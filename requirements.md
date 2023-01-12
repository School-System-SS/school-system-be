# Software Requirements
 
## Vision

Help schools ease the process of getting their students assignments and grading into one place, saving the planet, improving the education, and include the parents into the loop by providing a web management system.

## Scope (In/Out)

- IN - What will your product do
    - A web application that is responsible for managing students assignments and grades.

- OUT - What will your product not do.
  - At this stage it does not have a full HR system.

### Minimum Viable Product vs
 
What will your MVP functionality be?

- Landing page that contains the school’s information including where is it, the tuitions, curriculum, classes, and a way to contact us.

- We create a separate  panel dedicated to admins where the admin can create a new student account, assign them to their classes and create new teacher account and assign them to their classes, and can access to view their grades.

- There will be a section that contains all the classes that the student is enrolled in, once clicked on the class, there will be a section regarding assignments and its due dates, and another section for the grades.

- We developed a section that contains the classes, in each class the teacher will be able to assign home-works with due dates, and will be able to grade them.

What are your stretch goals?

- Parent panel.

- HR system.

- Finance system.

- Online exam functionality.

### Stretch
 
What stretch goals are you going to aim for?

- Parent panel.
 
## Functional Requirements
 
List the functionality of your product. This will consist of tasks such as the following:
 
1. Landing page that contains the school’s information including where is it, the tuitions, curriculum, classes, and a way to contact us.

2. We create a separate  panel dedicated to admins where the admin can create a new student account, assign them to their classes and create new teacher account and assign them to their classes, and can access to view their grades.

3. There will be a section that contains all the classes that the student is enrolled in, once clicked on the class, there will be a section regarding assignments and its due dates, and another section for the grades.

4. We developed a section that contains the classes, in each class the teacher will be able to assign home-works with due dates, and will be able to grade them.

### Data Flow

Once signed in a request will be conducted from the frontend to our RESTfull API to authenticate the user and authorize him/her inorder to give the user a specific view based on his/her permessions. Once the user is logged in "Student", he/she will see a list of courses that he/she is enrolled in, once clicked on a course a request will we sent to fetch the data for the assignments that the student has and will be redirected to the assignments view, if clicked on an assignment, the student then will be redirected to the submission field, where a request will before should be done to get the assignment's information and displays it on the screen, the student then will have the option to submit a pdf file as an attachment to the desired assignment and once submitted a post request will be done to the server to serialize the data and save the file into a specific location in the server, that should be retreived from the teacher if desired to grade the student. Once the user is done from turing around the web app, once clicked on log out, the local storage will be cleared out determining an unauthorized user where then will be redirected to the home page to browse the landing page.
 
## Non-Functional Requirements
 
Non-functional requirements are requirements that are not directly related to the functionality of the application but still important to the app.

Examples include:
1. Security; All passwords will be hashed and not accessed from anyone expect for the user, and each user will have a specific permession.
2. Usability; The project will be excuted using Next JS where the use of components make it reusable, along side the design can be customizable to match the clients theme, and it will be user friendly.