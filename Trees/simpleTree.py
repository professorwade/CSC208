from treelib import Tree, Node

def find(word):
    # Search tests
    print('Search for',word,': ',end='')
    count, found = word_tree.search(word)
    if found:
        print('\nFound it in', count, 'tries')
    else:
        print('\n',word,'not found in', count, 'words')

class WordBinaryTree:
    def __init__(self):
        self.tree = Tree()
        self.root_id = None
        self.search_count = 0

    def insert(self, word):
        if not self.root_id:
            self.root_id = word
            self.tree.create_node(tag=word, identifier=self.root_id, data={'left': None, 'right': None})
            return

        current_id = self.root_id
        while True:
            current_node = self.tree.get_node(current_id)
            current_word = current_node.tag

            if word == current_word:
                return  # Handle duplicates as needed
            elif word < current_word:
                if not current_node.data['left']:
                    new_id = f"{current_id}_left"
                    self.tree.create_node(tag=word, identifier=new_id, parent=current_id,
                                          data={'left': None, 'right': None})
                    current_node.data['left'] = new_id
                    self.tree.update_node(current_id, data=current_node.data)
                    break
                else:
                    current_id = current_node.data['left']
            else:
                if not current_node.data['right']:
                    new_id = f"{current_id}_right"
                    self.tree.create_node(tag=word, identifier=new_id, parent=current_id,
                                          data={'left': None, 'right': None})
                    current_node.data['right'] = new_id
                    self.tree.update_node(current_id, data=current_node.data)
                    break
                else:
                    current_id = current_node.data['right']

    def search(self, word):
        self.search_count = 0
        current_id = self.root_id
        while current_id:
            self.search_count = self.search_count + 1
            current_node = self.tree.get_node(current_id)
            print(current_node.tag,end=' / ')
            if word == current_node.tag:
                return self.search_count, True
            elif word < current_node.tag:
                current_id = current_node.data['left']
            else:
                current_id = current_node.data['right']
        return self.search_count, False

# Example usage
word_tree = WordBinaryTree()
random_words = [
    "guitar", "sunshine", "tranquility", "elephant", "ocean", "adventure", "horizon",
    "magnificent", "lantern", "forest", "yellow", "umbrella", "nostalgic", "diamond",
    "serene", "planet", "creative", "tree", "kindness", "radiant", "flower",
    "peaceful", "xylophone", "vibrant", "knowledge", "snowflake", "joyful",
    "delightful", "orange", "waterfall", "harmonious", "bravery", "mirror",
    "journey", "energy", "luminous", "artistic", "notebook", "candle",
    "optimistic", "violin", "wisdom", "galaxy", "quirky", "apple",
    "fantastic", "mountain", "zebra", "quietness", "explore",
    "yearning", "kite", "rainbow", "unique", "pencil", "lemon", "cherry",
    "banana", "dog", "ice", "jungle", "quartz", "island", "universe",
    "village", "xenon", "zephyr", "enthusiastic", "graceful", "imaginative",
    "thoughtful", "wonderful", "butterfly", "cloud", "dance", "eagle",
    "fountain", "glacier", "honeybee", "igloo", "jasmine", "kangaroo",
    "laughter", "mango", "nectar", "ostrich", "pineapple", "quail",
    "rabbit", "sunset", "tiger", "ukulele", "vacation", "walnut",
    "x-ray", "yacht", "zucchini", "acorn", "bouquet", "cactus",
    "daffodil", "emerald", "flamingo", "gargoyle", "hazard", "ivy",
    "jester", "kaleidoscope", "lullaby", "marble", "nectarine", "oak",
    "paprika", "quartzite", "rhinoceros", "saffron", "tornado", "uakari",
    "vulture", "wisteria", "xanthan", "yogurt", "zestful", "aardvark",
    "blossom", "calliope", "dolphin", "echidna", "flute", "giraffe",
    "hazelnut", "iris", "jade", "kumquat", "larch", "mocha", "nougat",
    "onyx", "papaya", "quokka", "radish", "sapphire", "toucan", "urchin",
    "valentine", "willow", "xanthosis", "yogic", "zinnia", "amethyst",
    "bronze", "cantaloupe", "dewdrop", "ebony", "fiddle", "garnet",
    "hibiscus", "iodine", "jicama", "kiwi", "labrador", "mahogany",
    "nectarine", "opal", "pomegranate", "quartzite", "rosemary", "sage",
    "tangerine", "umber", "violet", "waxwing", "xenophobia", "yarrow",
    "zest", "agate", "bougainvillea", "cassowary", "dahlia", "elderberry",
    "fig", "ginkgo", "hawthorn", "indigo", "jasper", "kohlrabi", "leopard",
    "magnolia", "nasturtium", "oatmeal", "pansy", "quince", "rhubarb",
    "sandalwood", "tansy", "uva", "vetch", "wallaby", "xeriscape", "yew",
    "zinfandel"
]

# put the words in the tree
for word in random_words:
    word_tree.insert(word)

print("Tree structure:")
word_tree.tree.show()

print('Inserted',len(random_words), 'random words')

find('lullaby')
find('zebra')
find('indigo')
find('unicorn')



