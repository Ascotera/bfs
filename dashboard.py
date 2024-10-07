import streamlit as st
from collections import deque
import pandas as pd

# Define the British royal family tree as a dictionary
royal_family_tree = {
    'Queen Elizabeth II': ['Charles', 'Anne', 'Andrew', 'Edward'],
    'Charles': ['William', 'Harry'],
    'Anne': ['Peter', 'Zara'],
    'Andrew': ['Beatrice', 'Eugenie'],
    'Edward': ['James', 'Louise'],
    'William': ['George', 'Charlotte', 'Louis'],
    'Harry': ['Archie'],
    'Peter': ['Savannah', 'Isla'],
    'Zara': ['Mia'],
    'Beatrice': ['Sienna'],
    'Eugenie': ['August'],
    'James': ['Viscount Severn'],
    'Louise': [],
    'George': [],
    'Charlotte': [],
    'Louis': [],
    'Archie': [],
    'Savannah': [],
    'Isla': [],
    'Mia': [],
    'Sienna': [],
    'August': [],
    'Viscount Severn': []
}

# Define the BFS function
def bfs_search(start, goal):
    visited = set()
    queue = deque([[start]])
    queue_process = []

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            if node == goal:
                queue_process.append({'Step': len(queue_process) + 1, 'Action': 'Dequeued', 'Path': ' -> '.join(path)})
                return path, queue_process

            for relative in royal_family_tree.get(node, []):
                new_path = list(path)
                new_path.append(relative)
                queue.append(new_path)
                queue_process.append({'Step': len(queue_process) + 1, 'Action': 'Enqueued', 'Path': ' -> '.join(new_path)})

            queue_process.append({'Step': len(queue_process) + 1, 'Action': 'Dequeued', 'Path': ' -> '.join(path)})

    return None, queue_process

# Create a Streamlit dashboard
st.title("Blind Search BFS Dashboard")

# Create a Tab
tab1, tab2 = st.tabs(["Dashboard", "Source code"])
 
with tab1:
    # Set the start node to 'Queen Elizabeth II'
    start_node = 'Queen Elizabeth II'

    # Add a selectbox to choose the goal node
    goal_node = st.selectbox("Select the goal node:", list(royal_family_tree.keys()))

    # Add a button to run the BFS search
    if st.button("Run BFS Search"):
        result, queue_process = bfs_search(start_node, goal_node)

        if result:
            st.write("Path found:", ' -> '.join(result))
        else:
            st.write("No path found")

        st.write("Queue process:")
        st.table(pd.DataFrame(queue_process))

with tab2:
    code = """# Define the British royal family tree as a dictionary
royal_family_tree = {
    'Queen Elizabeth II': ['Charles', 'Anne', 'Andrew', 'Edward'],
    'Charles': ['William', 'Harry'],
    'Anne': ['Peter', 'Zara'],
    'Andrew': ['Beatrice', 'Eugenie'],
    'Edward': ['James', 'Louise'],
    'William': ['George', 'Charlotte', 'Louis'],
    'Harry': ['Archie'],
    'Peter': ['Savannah', 'Isla'],
    'Zara': ['Mia'],
    'Beatrice': ['Sienna'],
    'Eugenie': ['August'],
    'James': ['Viscount Severn'],
    'Louise': [],
    'George': [],
    'Charlotte': [],
    'Louis': [],
    'Archie': [],
    'Savannah': [],
    'Isla': [],
    'Mia': [],
    'Sienna': [],
    'August': [],
    'Viscount Severn': []
}

# Define the BFS function
def bfs_search(start, goal):
    visited = set()
    queue = deque([[start]])
    queue_process = []

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            if node == goal:
                queue_process.append({'Step': len(queue_process) + 1, 'Action': 'Dequeued', 'Path': ' -> '.join(path)})
                return path, queue_process

            for relative in royal_family_tree.get(node, []):
                new_path = list(path)
                new_path.append(relative)
                queue.append(new_path)
                queue_process.append({'Step': len(queue_process) + 1, 'Action': 'Enqueued', 'Path': ' -> '.join(new_path)})

            queue_process.append({'Step': len(queue_process) + 1, 'Action': 'Dequeued', 'Path': ' -> '.join(path)})

    return None, queue_process"""
    st.code(code, language='python')