import socket
import ipaddress
import subprocess
import concurrent.futures
import random
import json
import platform
from tqdm import tqdm
from jarvis import Jarvis

# Configuration
specific_port = 12345  # The port to scan
max_weight = 10  # Maximum weight for edges
min_weight = 1  # Minimum weight for edges

# TODO sensor should not put other sensors distance in the adj list
def get_local_ip(public_address="8.8.8.8", public_port=80):
    """Retrieve the local IP address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((public_address, public_port))
            return s.getsockname()[0]
    except Exception as e:
        print(f"Error connecting to public address {public_address}:{public_port} - {e}")
        return "127.0.0.1"


def ping_ip(ip):
    """Ping the IP to check if it is active."""
    system_name = platform.system()
    if system_name == "Windows":
        result = subprocess.run(['ping', '-n', '1', '-w', '1000', str(ip)], stdout=subprocess.DEVNULL)
    elif system_name in ("Linux", "Darwin"):
        result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)], stdout=subprocess.DEVNULL)
    return ip if result.returncode == 0 else None


def scan_port(ip, port):
    """Check if the specific port is open on the given IP."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((str(ip), port))
            return port
    except:
        return None


def scan_ip(ip):
    """Scan the IP for the specific port."""
    if scan_port(ip, specific_port):
        return ip
    return None


def discover_nodes(network_range):
    active_ips = []

    # Step 1: Discover active IPs
    print(f"Scanning network for active IPs in range {network_range}...")
    ip_nums = ipaddress.IPv4Network(network_range).num_addresses
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        with tqdm(total=ip_nums, desc="Pinging IPs", unit="ip") as progress:
            futures = [executor.submit(ping_ip, ip) for ip in ipaddress.IPv4Network(network_range)]
            for future in concurrent.futures.as_completed(futures):
                ip = future.result()
                if ip:
                    print(f"Active IP found: {ip}")
                    active_ips.append(ip)
                progress.update(1)

    # Step 2: Scan each active IP for the specific port
    print(f"Scanning active IPs for port {specific_port}...")
    discovered_nodes = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_ip, ip) for ip in active_ips]
        for future in concurrent.futures.as_completed(futures):
            ip = future.result()
            if ip:
                print(f"Node discovered with port {specific_port} open: {ip}")
                discovered_nodes.append(ip)

    print(f"Discovered {len(discovered_nodes)} nodes with port {specific_port} open:")
    for node in discovered_nodes:
        print(node)
    return discovered_nodes


def build_adjacency_list(nodes):
    """Create a randomized adjacency list for the discovered nodes, excluding self-references."""
    adjacency_list = {}
    nodes = set(nodes)  # Ensure unique nodes
    for node in nodes:
        node_str = str(node)
        adjacency_list[node_str] = {}
        for neighbor in nodes:
            neighbor_str = str(neighbor)
            if node != neighbor:  # Exclude self-references
                adjacency_list[node_str][neighbor_str] = random.randint(min_weight, max_weight)
    return adjacency_list


def save_adjacency_list_to_file(adjacency_list, filename="adjacency_list.json"):
    """Save the adjacency list to a JSON file."""
    with open(filename, "w") as f:
        json.dump(adjacency_list, f, indent=4)
    print(f"Adjacency list saved to {filename}")


def share_adjacency_list(nodes, adjacency_list):
    """Share the adjacency list with all discovered nodes."""

    jarvis = Jarvis()

    for node in nodes:
        try:
            full_message = jarvis.build_message(str(node), str(json.dumps(adjacency_list)), 'routing-info')
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((str(node), specific_port))
                s.sendall(full_message)
                print(f"Shared adjacency list with node {node}")
        except Exception as e:
            print(f"Failed to share adjacency list with {node}: {e}")


# Main execution
if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"Local IP: {local_ip}")

    # Ask the user for the network range
    network_range = input("Enter the network range (e.g., 192.168.1.0/24): ").strip()

    # Discover nodes
    discovered_nodes = discover_nodes(network_range)
    #discovered_nodes.append(local_ip)

    # Build adjacency list if nodes are discovered
    if discovered_nodes:
        print("\nBuilding adjacency list...")
        adjacency_list = build_adjacency_list(discovered_nodes)
        print("\nGenerated Adjacency List:")
        for node, neighbors in adjacency_list.items():
            print(f"{node}: {neighbors}")

        # Save the adjacency list to a file
        save_adjacency_list_to_file(adjacency_list)

        # Share the adjacency list with all discovered nodes
        print("\nSharing adjacency list with discovered nodes...")
        share_adjacency_list(discovered_nodes, adjacency_list)
    else:
        print("No nodes with the specified port were discovered.")
