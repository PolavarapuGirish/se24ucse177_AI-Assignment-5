import networkx as nx
import matplotlib.pyplot as plt

def build_knowledge_graph():
    kg = nx.DiGraph()

    kg.add_edge("Student", "Artificial Intelligence", relation="studies")
    kg.add_edge("Student", "University", relation="enrolled_in")
    kg.add_edge("University", "Hyderabad", relation="located_in")
    kg.add_edge("Student", "Knowledge Graph", relation="learns")
    kg.add_edge("Knowledge Graph", "Neo4j", relation="implemented_using")
    kg.add_edge("Knowledge Graph", "Protégé", relation="modeled_using")

    return kg

if __name__ == "__main__":
    graph = build_knowledge_graph()

    print("Nodes:")
    print(list(graph.nodes()))

    print("\nRelationships:")
    for source, target, data in graph.edges(data=True):
        print(f"{source} --{data['relation']}--> {target}")

    plt.figure(figsize=(8, 6))

    pos = nx.spring_layout(graph)

    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=3000,
        font_size=9
    )

    edge_labels = nx.get_edge_attributes(graph, "relation")

    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=edge_labels
    )

    plt.title("Knowledge Graph Example")
    plt.show()
