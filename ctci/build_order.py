"""
Build Order: You are given a list of projects and a list of dependencies
(which is a list of pairs of projects where the second project is
dependent on the first project). All of a project's dependencies must be
built before the project is. Find a build order that will allow the
projects to be built. If there is no valid build order, return an error.

EXAMPLE
Input:
    projects = [a, b, c, d, e, f]
    dependencies = [(a, d), (f, b), (b, d), (f, a), (d, c)]
Output:
    f, e, a, b, d, c
"""


class Project:
    """Object for project to be built in a certain order"""

    def __init__(self, name):
        self.name = name
        self.dependencies = []
        self.dependents = []
        self.seen = False

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def add_dependent(self, dependent):
        self.dependents.append(dependent)


def build_order(projects, dependencies):
    """Find order to build projects while considering dependencies

    projects    : list of names of projects
    dependencies: adjacency list of projects and individual dependencies
    """
    # Variable to return
    results = []

    # Check if we're caught in circular dependencies
    cycle = False

    # Instantiate Project objects into a dictionary
    projects_dict = {}
    for project in projects:
        projects_dict[project] = Project(project)

    # Add dependencies to Project objects
    for dependency in dependencies:
        project = projects_dict[dependency[1]]
        project.add_dependency(dependency[0])

        dependent = projects_dict[dependency[0]]
        dependent.add_dependent(dependency[1])

    # Add projects without dependencies to build order and then
    # remove that project as a dependency from its dependents
    while len(projects_dict) > 0 and not cycle:
        cycle = True
        for project in projects_dict.values():
            if project.seen is False and len(project.dependencies) == 0:
                project.seen = True
                results.append(project.name)

                # Remove project as a dependency from its dependents
                for dependent in project.dependents:
                    dependent = projects_dict[dependent]
                    to_remove = dependent.dependencies
                    for item in to_remove:
                        dependent.dependencies.remove(item)

                cycle = False

        if cycle:
            return ValueError("ValueError: Input contains circular dependencies")

        # Remove tracked projects from dictionary
        for result in results:
            if result in projects_dict and len(projects_dict[result].dependencies) == 0:
                del projects_dict[result]

    return results


###########
# Testing #
###########
projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
results = build_order(projects, dependencies)
assert results == ["e", "f", "a", "b", "d", "c"]

projects.append("h")
projects.append("g")
dependencies = [
    ("d", "g"),
    ("f", "c"),
    ("f", "b"),
    ("f", "a"),
    ("c", "a"),
    ("b", "a"),
    ("b", "h"),
    ("b", "e"),
    ("a", "e"),
]
results = build_order(projects, dependencies)
assert results == ["d", "f", "g", "b", "c", "h", "a", "e"]

projects = ["a", "b"]
dependencies = [("a", "b"), ("b", "a")]
results = build_order(projects, dependencies)
assert isinstance(results, ValueError)
