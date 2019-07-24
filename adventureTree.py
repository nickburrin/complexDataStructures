class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while len(story_node.choices) > 0:
            choice = input("Enter 1 or 2 to continue the story: ")
            while choice not in ['1', '2']:
                choice = input("Enter a valid choice (1 or 2): ")
            chosen_index = int(choice)
            chosen_child = story_node.choices[chosen_index-1]
            print(chosen_child.story_piece)
            story_node = chosen_child