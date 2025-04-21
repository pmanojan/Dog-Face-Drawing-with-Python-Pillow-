import matplotlib.pyplot as plt
import networkx as nx

def draw_fungal_algal_flowchart():
    G = nx.DiGraph()
    
    # Define nodes for Fungal and Algal Insulin Production
    nodes = {
        "Start": (0, 10),
        "Fungal-Based Insulin Production": (-3, 9),
        "Genetic Engineering (Fungal)": (-3, 8),
        "Fermentation & Cultivation (Fungal)": (-3, 7),
        "Insulin Production & Processing (Fungal)": (-3, 6),
        "Purification & Formulation (Fungal)": (-3, 5),
        "Algal-Based Insulin Production": (3, 9),
        "Genetic Transformation (Algal)": (3, 8),
        "Cultivation Conditions (Algal)": (3, 7),
        "Insulin Extraction & Purification (Algal)": (3, 6),
        "Purification & Storage (Algal)": (3, 5),
        "End": (0, 4)
    }
    
    # Add nodes to graph
    for node, pos in nodes.items():
        G.add_node(node, pos=pos)
    
    # Define edges
    edges = [
        ("Start", "Fungal-Based Insulin Production"),
        ("Fungal-Based Insulin Production", "Genetic Engineering (Fungal)"),
        ("Genetic Engineering (Fungal)", "Fermentation & Cultivation (Fungal)"),
        ("Fermentation & Cultivation (Fungal)", "Insulin Production & Processing (Fungal)"),
        ("Insulin Production & Processing (Fungal)", "Purification & Formulation (Fungal)"),
        ("Purification & Formulation (Fungal)", "End"),
        ("Start", "Algal-Based Insulin Production"),
        ("Algal-Based Insulin Production", "Genetic Transformation (Algal)"),
        ("Genetic Transformation (Algal)", "Cultivation Conditions (Algal)"),
        ("Cultivation Conditions (Algal)", "Insulin Extraction & Purification (Algal)"),
        ("Insulin Extraction & Purification (Algal)", "Purification & Storage (Algal)"),
        ("Purification & Storage (Algal)", "End")
    ]
    
    # Add edges to graph
    G.add_edges_from(edges)
    
    # Draw graph
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', edge_color='black', font_size=8, font_weight='bold', arrows=True)
    plt.title("Flowchart of Fungal and Algal Insulin Production")
    plt.show()

def draw_insect_cell_flowchart():
    G = nx.DiGraph()
    
    # Define nodes with positions
    nodes = {
        "Start": (0, 7),
        "Genetic Engineering": (0, 6),
        "Baculovirus Construction": (0, 5),
        "Transfection & Amplification": (0, 4),
        "Insect Cell Culture": (0, 3),
        "Insulin Expression": (0, 2),
        "Cell Lysis & Extraction": (0, 1),
        "Purification & Refolding": (0, 0),
        "Formulation & Storage": (0, -1),
        "End": (0, -2)
    }
    
    # Add nodes to the graph
    for node, pos in nodes.items():
        G.add_node(node, pos=pos)
    
    # Define edges
    edges = [
        ("Start", "Genetic Engineering"),
        ("Genetic Engineering", "Baculovirus Construction"),
        ("Baculovirus Construction", "Transfection & Amplification"),
        ("Transfection & Amplification", "Insect Cell Culture"),
        ("Insect Cell Culture", "Insulin Expression"),
        ("Insulin Expression", "Cell Lysis & Extraction"),
        ("Cell Lysis & Extraction", "Purification & Refolding"),
        ("Purification & Refolding", "Formulation & Storage"),
        ("Formulation & Storage", "End")
    ]
    
    # Add edges to the graph
    G.add_edges_from(edges)
    
    # Draw graph
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(8, 10))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', edge_color='black', font_size=10, font_weight='bold', arrows=True)
    plt.title("Flowchart of Insect Cell-Based Insulin Production")
    plt.show()

# Call functions to draw the flowcharts
draw_fungal_algal_flowchart()
draw_insect_cell_flowchart()
