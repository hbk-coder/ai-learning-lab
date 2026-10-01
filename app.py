import json
from typing import Any

def menu_display() -> None:
    print("Program Menu")
    print("1. Add")
    print("2. Show")
    print("3. Edit")
    print("4. Delete")
    print("5. Report")
    print("6. Exit")
    
def data_entry(id: int) -> dict[str, Any]:
    full_name: str = input("Please enter your full name: ").strip().title()
    email: str = input("Please enter your email: ").strip().lower()
    city: str = input("Please enter your city: ").strip().title()
    education_degree: str = input("Please enter your education degree: ").strip().lower()
    education_field: str = input("Please enter your education field: ").strip().lower()
    skills: list[dict] = skill_entry()
    
    return dict(
        id= id,
        full_name= full_name,
        email= email,
        city= city,
        education=
            dict(
                degree= education_degree,
                field= education_field
                ),
        skills= skills
        )
    
def skill_entry() -> list[dict[str, Any]]:
    skills: list[dict] = []
    
    while True:
        skill_dict: dict[str, str] = {}
        skill_dict["name"] = input("Please enter your skill name: ").strip().title()
        skill_dict["level"] = input("Please enter your skill level: ").strip()
        
        while True:
            try:
                score: float = float(input("Please enter your skill score (between 0-100): "))
                if not 0 <= score <= 100:
                    print("Please enter a number between 0-100")
                else:
                    break
            except ValueError:
                print("Please enter a valid number")
        skill_dict["score"] = score
        
        skills.append(skill_dict)
        
        
        while True:
            add_skill: str = input("Do you want to add a new skill? (Yes/No): ").strip().lower()
            if add_skill == "yes" or add_skill == "no":
                break
            else:
                print("Please enter Yes or No!")
        if add_skill == "no":
            break
        
    return skills
   
def add_karvand(karvands) -> list[dict[str, Any]]:
    id: int = max([k.get("id", 0) for k in karvands], default=0) + 1
    new_karvand: dict[str, str] = data_entry(id)
    karvands.append(new_karvand)
    
    return karvands
    
def show_karvands(karvands) -> None:
    if not karvands:
        print("No karvands registered yet!")
        return
     
    for index, karvand in enumerate(karvands, 1):
        print(f"{index}: {karvand['full_name']}")

def input_list_display(karvands) -> None:
    if not karvands:
        return
    
    key_list: list[str] = [key.replace("_", " ").title() for key in karvands[0].keys()]

    for index, key in enumerate(key_list[1:4], 1):
        print(f"{index}: {key}")
        
def target_karvand_entry(karvands) -> tuple[str, int | None]:
    target_karvand: str = input("Please enter the name of the karvand: ").strip().title()
    found_index: int | None = None
    
    for index, karvand in enumerate(karvands):
        
        if karvand.get("full_name") == target_karvand:
            found_index = index
            break
        
    
    return target_karvand, found_index
        
        
def edit_karvand(karvands) -> list[dict]:
    if not karvands:
        print("No karvands registered yet!")
        return karvands
    
    target_karvand, found_index = target_karvand_entry(karvands)
    
    if found_index == None:
            print(f"There is no karvand by name {target_karvand} in this bootcamp!")
            return karvands
    
    input_list_display(karvands)
    
    while True:
        required_edit: str = input(f"What information do you want to edit for {target_karvand}? Please enter from list above: ").strip().lower()
        match required_edit:
            case "full name":
                new_full_name: str = input("Please enter a new full name: ").strip().title()
                karvands[found_index]["full_name"] = new_full_name
                break
            case "email":
                new_email: str = input("Please enter a new email: ").strip().lower()
                karvands[found_index]["email"] = new_email
                break
            case "city":
                new_city: str = input("Please enter a new city: ").strip().title()
                karvands[found_index]["city"] = new_city
                break
            case _:
                print("Please enter a valid option in the list: ")
                input_list_display(karvands)
    
    return karvands

def delete_karvand(karvands) -> list[dict]:
    if not karvands:
        print("No karvands registered yet!")
        return karvands
    
    target_karvand, found_index = target_karvand_entry(karvands)
    
    if found_index == None:
            print(f"There is no karvand by name {target_karvand} in this bootcamp!")
            return karvands    
    
    del karvands[found_index]
    print(f"\nKarvand '{target_karvand}' removed and saved successfully.")
    return karvands
    
    
def main():
    bootcamp: dict[str] = dict(title = "karvand Python", year = 2026)
    karvands: list[dict] = []
    
    while True:
        menu_display()
        item_selected: str = input("Please enter an item from the above list: ").strip().lower()
        
        match item_selected:
            case "add":
                karvands = add_karvand(karvands)
            case "show":
                show_karvands(karvands)
            case "edit":
                karvands = edit_karvand(karvands)
            case "delete":
                karvands = delete_karvand(karvands)
            case "report":
                report = dict(bootcamp = bootcamp, karvands = karvands)
                print(json.dumps(report, indent=4, ensure_ascii= False))
            case "exit":
                print("Have a good day!")
                return
            case _:
                print("Please enter a valid item!")
                
                
    
    
    
if __name__ == "__main__":
    main()