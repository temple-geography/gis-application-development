# GIS Application Development

Schedule of workshops for a graduate course in application development focusing on GIS and geospatial applications.

This course makes use of [*Practices of the Python Pro*](https://www.manning.com/books/practices-of-the-python-pro) by Dane Hillard (Manning Press).

The easiest way to get all packages necessary for these workshops is to download to download the conda environment file [gus8066-environment.yml](gus8066-environment.yml) and run the following command in the Anaconda Prompt:

```sh
conda env create -f gus8066-environment.yml
```

The environment file includes the Spyder IDE. If you prefer another IDE, you can comment out or delete that line before creating the environment. If you prefer working with Jupyter notebooks you can add `- jupyter` to the list of dependencies, or install it after environment creating with `conda install jupyter`.

## Schedule

* Week 1 - Introduction
    * Readings
        * :closed_book: *PotPP* Ch 1 - The bigger picture
        * :closed_book: [Agile vs. waterfall project management](https://www.atlassian.com/agile/project-management/project-management-intro)
        * :closed_book: [Agile workflows](https://www.atlassian.com/agile/project-management/workflow)
    * :hammer_and_wrench: [Workshop: Introduction to Git and GitHub](introduction_to_git/introduction_to_git.md)
    * :rocket: Introduce project topics, discuss student interests
* Week 2 - Version Control
    * Readings
        * :closed_book: *PotPP* Ch 2 - Separation of concerns
        * :closed_book: [Stories, epics, and initiatives](https://www.atlassian.com/agile/project-management/epics-stories-themes)
        * :closed_book: [Agile epics: definition, examples, and templates](https://www.atlassian.com/agile/project-management/epics)
        * :closed_book: [User stories with examples and a template](https://www.atlassian.com/agile/project-management/user-stories)
        * :closed_book: [Story points and estimation](https://www.atlassian.com/agile/project-management/estimation)
    * :hammer_and_wrench: [Workshop: Creating Classes in Python](classes_and_oop/creating_classes_in_python.md)
    * :rocket: Finalize project teams, begin creating epics and user stories
* Week 3 - Classes and Object-Oriented Programming
    * Readings
        * :closed_book: *PotPP* Ch 3 - Abstraction and Encapsulation
    * :hammer_and_wrench: Workshop: Functions and Modules
    * :rocket: Sprint 0 - Create epics and user stories
* Week 4 - Time Complexity
    * Readings
        * :closed_book: *PotPP* Ch 4 - Designing for high performance
    * :hammer_and_wrench: [Workshop: Timing and CPU Profiling](time_space_complexity/time_complexity.md)
    * :rocket: Sprint 0 (cont.) - Finish epics and user stories, populate epic backlog
* Week 5 - Database Access
    * :hammer_and_wrench: [Workshop: SQLAlchemy and Other Python Packages for Database Access](database_access/data_access.md)
    * :rocket: Sprint 1
* Week 6 - Testing
    * Readings
        * :closed_book: *PotPP* Ch 5 - Testing your Software
    * :hammer_and_wrench: Workshop: Python unittest
    * :rocket: Sprint 1 (cont.)
* Week 7 - GUI Design
    * :hammer_and_wrench: [Workshop: PyQt and Qt Designer](gui_design/gui_design_workshop_notes.md)
    * :rocket: Sprint 2
* Week 8 - Web Applications and Dashboards
    * :hammer_and_wrench: Workshop: Flask or Django
    * :rocket: Sprint 2 (cont.)
* Week 9 - Documentation
    * :hammer_and_wrench: Workshop: Using Sphinx for Python Documentation
    * :rocket: Sprint 3
* Week 10 - Distributing Software
    * :hammer_and_wrench: Workshop: Packaging/Freezing in Python
    * :rocket: Sprint 3 (cont.)
* Weeks 11-12 - Term Project
    * :rocket: Sprint 4
* Weeks 13-14 - Term Project
    * :rocket: Freezing/Packaging & Documentation




