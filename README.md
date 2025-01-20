# smart_organizer
# Smart Organizer Documentation

## Overview
Smart Organizer is a web-based task management application designed to simplify task organization and tracking. It features a clean, professional design and an intuitive user interface, making it suitable for individual and collaborative workflows. The application is built using HTML, CSS, and Django templating, with scalability and integration in mind.

## Features
1. **Display Tasks**:
   - Lists all tasks with details such as title, deadline, priority, and completion status.
   - Highlights overdue tasks and provides alerts when necessary.

2. **Add Tasks**:
   - Allows users to create tasks by specifying a title, deadline, and priority (High, Medium, Low).
   - Includes form validation for required fields.

3. **Mark Tasks as Complete**:
   - Enables users to select tasks and mark them as complete via a simple checkbox interface.

## Project Structure
### HTML Files
1. **profile.html**:
   - Acts as the dashboard, offering navigation links to the other features (Display Tasks, Add Tasks, Mark Tasks as Complete).
   - Designed with a consistent theme for a premium user experience.

2. **display_tasks.html**:
   - Lists all tasks with dynamic data passed via the backend.
   - Includes logic to display tasks as "Complete" or "Pending" and triggers alerts for overdue tasks.

3. **add_task.html**:
   - Contains a form for creating new tasks.
   - Provides input fields for task title, deadline, and priority, ensuring user-friendly input.

4. **mark_complete.html**:
   - Displays a list of tasks with checkboxes to select and mark tasks as complete.

### CSS File
- **style.css**:
   - Implements a professional and cohesive theme across all pages.
   - Focuses on a clean, modern design with responsive layouts.
   - Features consistent typography, button styling, and form elements to enhance user experience.

## Backend Integration (Django Templating)
- **Dynamic Content Rendering**: Utilizes Django templating to populate task data dynamically.
- **CSRF Protection**: Ensures secure handling of form submissions.

## How to Run the Application
1. Clone the repository to your local machine.
2. Ensure Python and Django are installed in your environment.
3. Run the Django development server with:
   ```
   python manage.py runserver
   ```
4. Open your browser and navigate to the server's URL (default: `http://127.0.0.1:8000`).

## Future Enhancements
- Adding user authentication for personalized task management.
- Integrating reminders and notifications for upcoming deadlines.
- Enabling collaboration features such as shared task lists and real-time updates.

## Conclusion
Smart Organizer is a robust foundation for task management applications and demonstrates the potential to scale into a comprehensive organizational tool. Its clean design and efficient features align well with the goals of building versatile software solutions.

