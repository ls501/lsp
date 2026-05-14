class BullyAlgorithm:

    def __init__(self, nodeId, nodes):
        self.nodeId = nodeId
        self.nodes = nodes

    def startElection(self):

        highestNodeId = self.nodeId

        # Send "Coordinator Election" messages
        for i in range(self.nodeId + 1, len(self.nodes) + 1):

            if i in self.nodes:
                print(f"Node {self.nodeId} sends Coordinator Election message to Node {i}")

        # Wait for "OK" messages
        for i in range(self.nodeId + 1, len(self.nodes) + 1):

            if i in self.nodes:
                print(f"Node {self.nodeId} waiting for OK message from Node {i}")

        # Check for higher ID responses
        for i in range(self.nodeId + 1, len(self.nodes) + 1):

            if i in self.nodes:
                print(f"Node {self.nodeId} received OK message from Node {i}")
                highestNodeId = i

        # Send coordinator message
        if highestNodeId != self.nodeId:

            print(f"Node {self.nodeId} sends Coordinator message to Node {highestNodeId}")

        else:
            print(f"Node {self.nodeId} is the new coordinator")


# Create node list
nodes = [1, 2, 3, 4, 5]

# Create Bully Algorithm object
bully = BullyAlgorithm(3, nodes)

# Start election
bully.startElection()