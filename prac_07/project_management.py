from project import Project

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header line
        for line in file:
            parts = line.strip().split("\t")
            cost_estimate = float(parts[3])
            percentage = int(parts[4])
            project = Project(parts[0], parts[1], parts[2], cost_estimate, percentage)
            projects.append(project)
    return projects

def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

def filter_projects_by_date(projects, start_date):
    filtered_projects = [project for project in projects if project.start_date > start_date]
    for project in filtered_projects:
        print(f"{project}")

def add_new_project():
    name = input("Name: ")
    start_date = input("Start Date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost Estimate: "))
    completion_percentage = int(input("Completion Percentage: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    return project

def update_project(projects):
    display_projects(projects)
    index = int(input("Project choice: "))
    project = projects[index]
    new_completion_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    project.completion_percentage = new_completion_percentage
    project.priority = new_priority

def show_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

def main():
    filename = "projects.txt"
    print("Welcome to Pythonic Project Management")
    projects = load_projects(filename)
    while True:
        show_menu()
        choice = input(">>> ").upper()
        if choice == "L":
            projects = load_projects(filename)
        elif choice == "S":
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            start_date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, start_date)
        elif choice == "A":
            project = add_new_project()
            projects.append(project)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            save_option = input("Would you like to save to projects.txt? ").lower()
            if save_option.startswith("y"):
                save_projects(filename, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




