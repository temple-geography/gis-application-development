# GIS Application Development

Schedule of workshops for a graduate course in application development focusing on GIS and geospatial applications.

This course makes use of [*The Well-Grounded Python Developer*](https://www.manning.com/books/the-well-grounded-python-developer) by Doug Farrell (Manning Press).

The easiest way to get all packages necessary for these workshops is to download the conda environment file [gus8066-environment.yml](gus8066-environment.yml) and run the following command in the Anaconda Prompt:

```sh
conda env create -f gus8066-environment.yml
```

I recommend setting the package channel to conda-forge as follows:

```
conda activate gus8066
conda config --add channels conda-forge
conda config --set channel_priority strict
```

We will be using Visual Studio Code in this class. If you prefer working with Jupyter notebooks you can install it after creating the environment with `conda install jupyterlab notebook`.

## Schedule

* Week 1 - Introduction & Version Control
    * Readings
        * :closed_book: *WGPD* Ch 1 - Becoming a Pythonista
        * :closed_book: [Agile vs. waterfall project management](https://www.atlassian.com/agile/project-management/project-management-intro)
        * :closed_book: [Agile workflows](https://www.atlassian.com/agile/project-management/workflow)
    * :hammer_and_wrench: [Workshop: Introduction to Git and GitHub](introduction_to_git/introduction_to_git.md)
    * :rocket: Introduce project topics, discuss student interests
* Week 2 - Project Management & Programming Building Blocks
    * Readings
        * :closed_book: *WGPD* Ch 2 - That's a good name
        * :closed_book: *WGPD* Ch 3 - The API: Let's talk
        * :closed_book: [Stories, epics, and initiatives](https://www.atlassian.com/agile/project-management/epics-stories-themes)
        * :closed_book: [Agile epics: definition, examples, and templates](https://www.atlassian.com/agile/project-management/epics)
        * :closed_book: [User stories with examples and a template](https://www.atlassian.com/agile/project-management/user-stories)
        * :closed_book: [Story points and estimation](https://www.atlassian.com/agile/project-management/estimation)
    * :hammer_and_wrench: [Workshop: Functions and Modules](functions_and_modules/functions_and_modules.md)
    * :rocket: Finalize project teams, begin creating epics and user stories
* Week 3 - Classes and Object-Oriented Programming
    * Readings
        * :closed_book: *WGPD* Ch 4 - The object of conversation
    * :hammer_and_wrench: [Workshop: Creating Classes in Python](classes_and_oop/creating_classes_in_python.md)
    * :rocket: Sprint 0 - Create epics and user stories
* Week 4 - Time Complexity
    * Readings
        * :closed_book: ???
    * :hammer_and_wrench: [Workshop: Timing and CPU Profiling](time_space_complexity/time_complexity.md)
    * :rocket: Sprint 0 (cont.) - Finish epics and user stories, populate epic backlog
* Week 5 - Database Access
    * Readings
        * :closed_book: *WGPD* Ch 10 - Persistence is good: Databases
    * :hammer_and_wrench: [Workshop: SQLAlchemy and Other Python Packages for Database Access](database_access/intro_sqlalchemy.md)
    * :rocket: Sprint 1
* Week 6 - Testing
    * Readings
        * :closed_book: *WGPD* Section 12.1 - "Testing" (very short)
        * :closed_book: [Effective Python Testing With pytest](https://realpython.com/pytest-python-testing/) - focus on "What Makes pytest So Useful?" and "Paremetrization: Combining Tests"
    * :hammer_and_wrench: [Workshop: Unit testing with pytest](unit_testing/unit_testing_demo.md)
    * :rocket: Sprint 1 (cont.)
* Week 7 - GUI Design
    * :hammer_and_wrench: [Workshop: PyQt and Qt Designer](gui_design/gui_design_workshop_notes.md)
    * :rocket: Sprint 2
* Week 8 - Web Applications and Dashboards
    * Readings
        * :closed_book: *WGPD* Ch 6 - Sharing with the internet
        * :closed_book: *WGPD* Ch 7 - Doing it with style
    * :hammer_and_wrench: Workshop: Flask
    * :rocket: Sprint 2 (cont.)
* Week 9 - Documentation
    * Readings
        * :closed_book: Hillard 8?
    * :hammer_and_wrench: [Workshop: Using Sphinx for Python Documentation](documentation/sphinx_getting_started.md)
    * :rocket: Sprint 3
* Week 10 - Distributing Software
    * :hammer_and_wrench: [Workshop: Packaging in Python](distributing_software/packaging.md)
    * :hammer_and_wrench: [Workshop: Freezing an Application with PyInstaller](distributing_software/freezing.md)
    * :rocket: Sprint 3 (cont.)
* Weeks 11-12 - Term Project
    * :rocket: Sprint 4
* Weeks 13-14 - Term Project
    * :rocket: Freezing/Packaging & Documentation




