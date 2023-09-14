from bs4 import BeautifulSoup


def find_unique_elements_in_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        # Read the HTML file and parse it with BeautifulSoup
        soup = BeautifulSoup(file, 'html.parser')

        # Find all HTML elements and extract their tags
        elements = [element.name for element in soup.find_all()]

        # Get the unique elements as a list
        unique_elements = list(set(elements))

        return unique_elements, len(unique_elements)


if __name__ == "__main__":
    html_file = "C:/Users/megan/SchoolWork/CS2250/Homework_1/index.html"  # Replace with the path to your HTML file
    unique_elements, unique_count = find_unique_elements_in_html(html_file)

    print(f"Number of unique elements in the HTML file: {unique_count}")
    print(f"List of unique elements: {unique_elements}")
