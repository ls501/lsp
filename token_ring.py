class TokenRing:

    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.nodes = [None] * num_nodes

    def set_node(self, node_id, data):
        self.nodes[node_id] = data

    def run(self):

        token = self.nodes
        current_node = 0

        while True:

            # Check if the token is received
            if token:
                print(f"Node {current_node}: Received token with data '{token}'")

            # Process the token or perform some action
            print(f"Node {current_node}: Processing data '{self.nodes[current_node]}'")

            # Pass the token to the next node
            next_node = (current_node + 1) % self.num_nodes

            token = self.nodes[next_node]
            self.nodes[next_node] = None

            # Break if the token completes a full rotation
            if current_node == 0 and token is None:
                break

            # Move to the next node
            current_node = next_node


# Create an instance of TokenRing with 4 nodes
token_ring = TokenRing(4)

# Set the data for each node
token_ring.set_node(0, "Data 1")
token_ring.set_node(1, "Data 2")
token_ring.set_node(2, "Data 3")
token_ring.set_node(3, "Data 4")

# Run the token ring algorithm
token_ring.run()