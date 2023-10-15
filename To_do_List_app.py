class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def mark_item_as_done(self, item):
        item.is_done = True

    def get_all_items(self):
        return self.items

    def get_incomplete_items(self):
        incomplete_items = []
        for item in self.items:
            if not item.is_done:
                incomplete_items.append(item)
        return incomplete_items

class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_done = False

def main():
    to_do_list = TodoList()

    # Add some items to the to-do list
    to_do_list.add_item(TodoItem("Finish homework"))
    to_do_list.add_item(TodoItem("Clean my room"))
    to_do_list.add_item(TodoItem("Go to the gym"))

    # Mark the first item as done
    to_do_list.mark_item_as_done(to_do_list.items[0])

    # Print all of the incomplete items
    incomplete_items = to_do_list.get_incomplete_items()
    for item in incomplete_items:
        print(item.description)

if __name__ == "__main__":
    main()
