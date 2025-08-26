# Personal Blog & Portfolio

This is a simple personal blog & portfolio project built with Django, HTML, and CSS. It's designed to showcase projects and blog posts, present a résumé (as an HTML page), accept comments (admin-approved), and receive contact messages by email. There is no user authentication—visitors provide their name and email when they comment or send messages.

## Features

### Posts

- **Two types:** project and blog.
- **Fields:** title, content, image, related_url, slug, is_published, timestamps.
- Attach documents and images to posts.

### Comments & Replies

- Visitors submit comments with their name, email, and message.
- Comments are saved with `is_approved = False` and must be approved by an admin.
- An admin can create a single reply per comment (one-to-one).

### Contact Form

- Visitors send a message (name, email, message).
- Messages are sent to an admin email using Django's `send_mail` function.

### Résumé Page

- A dedicated template renders your résumé as an HTML file.

### Simple Admin Management

- Use the Django admin interface to create/edit posts, approve comments, add replies, and upload documents.

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, FontAwesome
- **Database (dev):** SQLite (changeable to PostgreSQL/MySQL for production)
- **Email:** Django `send_mail` (configure SMTP in settings)
- **Requirements:** `requirements.txt` is included.

## Models (summary)

- **Post:** `post_type`, `title`, `content`, `image`, `related_url`, `slug`, `is_published`, `published_at`, `created_at`, `updated_at`
- **Comment:** `email`, `full_name`, `content`, `post` (FK), `is_approved`, `created_at`
- **Reply:** `comment` (OneToOne), `content`, `created_at`
- **Document:** `title`, `file`, `image`, `uploaded_at`, `post` (FK)

## Installation & Local Setup

Clone, create a virtual environment, and install dependencies:

```sh
git clone [https://github.com/yourusername/yourproject.git](https://github.com/yourusername/yourproject.git)
cd yourproject

python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

License
This project is created by Kaveh. You may reuse or modify it for personal projects. If you want a specific license, add one (e.g., MIT) to the repository.

Contact
If you want to see the project live or ask questions, contact: davodabadikaveh@gmail.com (replace with your preferred contact).