import pandas as pd
class contacts:

    def __init__(self):
        self.list = list()
        #self.dataframe = pd.DataFrame(columns=["Name", "Contact"])
    
    def add_contact(self, name, contact):
        """

        Args:
            name ([str]): [this is the name of the friends to be added to the list]
            contact ([int]): [contacts of each friends]
        """
        self.name = name
        self.contact = contact

        # checks the instance or type of name, it has to be str type
        if isinstance(self.name, str) and self.name not in self.list:
            self.list.extend([self.name, self.contact])
            return self.list
        elif type(self.name) != str:
            print(f"Name {self.name} should be string datatype")
            return False
        # checks if the name is inside the list, if there does forceful appending
        elif self.name in self.list:
            print(f"You already have a friend with the name {self.name}")
            force_add = input("Do you have two friends with the same name, enter (Y/N) ")
            if force_add == "Y" or force_add == "y" and self.contact not in self.list:
                self.list.extend([self.name, self.contact])
                print("Your friend list has been updated already")
                return self.list
            else:
                return "We suspect a duplicate data in your list, you have same person with same contact"
        else:
            return self.list
    # Method for viewing or showing the diary
    def view_contact(self):
        return self.list
    # def contact_show(self):
    #     self.contact_df = pd.DataFrame(
    #         {'Name' : self.name,
    #         "Contact" : self.contact}, index = [0]
    #     )

    #     self.concat_df = pd.concat([self.dataframe, self.contact_df], axis=0, ignore_index=True)
    #     return "DataFrame Created", self.concat_df



if __name__ == "__main__":
    diary = contacts()
    contact_one = diary.add_contact(name="Victor O", contact=234567890)
    contact_two = diary.add_contact(name="Victor Opeyemi", contact=234567891)
    contact_three = diary.add_contact(name="Precious Adigun",contact=2347040508748)
    print(diary.view_contact())

