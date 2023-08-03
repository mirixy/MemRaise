import csv
class Presidents:
    def __init__(self):
        
        self.presidents = [
                {"number": 1, "name": "George Washington", "term": "1789-1797"},
                {"number": 2, "name": "John Adams", "term": "1797-1801"},
                {"number": 3, "name": "Thomas Jefferson", "term": "1801-1809"},
                {"number": 4, "name": "James Madison", "term": "1809-1817"},
                {"number": 5, "name": "James Monroe", "term": "1817-1825"},
                {"number": 6, "name": "John Quincy Adams", "term": "1825-1829"},
                {"number": 7, "name": "Andrew Jackson", "term": "1829-1837"},
                {"number": 8, "name": "Martin Van Buren", "term": "1837-1841"},
                {"number": 9, "name": "William Henry Harrison", "term": "1841"},
                {"number": 10, "name": "John Tyler", "term": "1841-1845"},
                {"number": 11, "name": "James K. Polk", "term": "1845-1849"},
                {"number": 12, "name": "Zachary Taylor", "term": "1849-1850"},
                {"number": 13, "name": "Millard Fillmore", "term": "1850-1853"},
                {"number": 14, "name": "Franklin Pierce", "term": "1853-1857"},
                {"number": 15, "name": "James Buchanan", "term": "1857-1861"},
                {"number": 16, "name": "Abraham Lincoln", "term": "1861-1865"},
                {"number": 17, "name": "Andrew Johnson", "term": "1865-1869"},
                {"number": 18, "name": "Ulysses S. Grant", "term": "1869-1877"},
                {"number": 19, "name": "Rutherford B. Hayes", "term": "1877-1881"},
                {"number": 20, "name": "James A. Garfield", "term": "1881"},
                {"number": 21, "name": "Chester A. Arthur", "term": "1881-1885"},
                {"number": 22, "name": "Grover Cleveland", "term": "1885-1889"},
                {"number": 23, "name": "Benjamin Harrison", "term": "1889-1893"},
                {"number": 24, "name": "Grover Cleveland", "term": "1893-1897"},
                {"number": 25, "name": "William McKinley", "term": "1897-1901"},
                {"number": 26, "name": "Theodore Roosevelt", "term": "1901-1909"},
                {"number": 27, "name": "William Howard Taft", "term": "1909-1913"},
                {"number": 28, "name": "Woodrow Wilson", "term": "1913-1921"},
                {"number": 29, "name": "Warren G. Harding", "term": "1921-1923"},
                {"number": 30, "name": "Calvin Coolidge", "term": "1923-1929"},
                {"number": 31, "name": "Herbert Hoover", "term": "1929-1933"},
                {"number": 32, "name": "Franklin D. Roosevelt", "term": "1933-1945"},
                {"number": 33, "name": "Harry S. Truman", "term": "1945-1953"},
                {"number": 34, "name": "Dwight D. Eisenhower", "term": "1953-1961"},
                {"number": 35, "name": "John F. Kennedy", "term": "1961-1963"},
                {"number": 36, "name": "Lyndon B. Johnson", "term": "1963-1969"},
                {"number": 37, "name": "Richard Nixon", "term": "1969-1974"},
                {"number": 38, "name": "Gerald Ford", "term": "1974-1977"},
                {"number": 39, "name": "Jimmy Carter", "term": "1977-1981"},
                {"number": 40, "name": "Ronald Reagan", "term": "1981-1989"},
                {"number": 41, "name": "George H. W. Bush", "term": "1989-1993"},
                {"number": 42, "name": "Bill Clinton", "term": "1993-2001"},
                {"number": 43, "name": "George W. Bush", "term": "2001-2009"},
                {"number": 44, "name": "Barack Obama", "term": "2009-2017"},
                {"number": 45, "name": "Donald Trump", "term": "2017-2021"},
                {"number": 46, "name": "Joe Biden", "term": "2021-present"}
            ]

    
    def save_csv(self):
        with open("presidents.csv", "w") as file:
            writer = csv.DictWriter(file,fieldnames=["name", "term"])
            writer.writeheader()
            for president in self.presidents:
                writer.writerow({"name": president['name'], "term": president['term']})
                
    def create_match_set(self):
        matches = {president["number"]: president["name"] for president in self.presidents}
        return matches


def main():
    ...





if __name__ == "__main__":
    main