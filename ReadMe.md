What the prototype includes (core features from your design):

Three user roles: Supplier, Buyer, Admin

Authentication: Registration, login, role‑based access

Product management: Create/update listings with condition grades (A, B, C, D), images, bulk CSV upload

Browse & filter: Search by category, grade, price range, supplier country

Order workflow: Cart → order placement → supplier confirmation → status tracking

Mock payment: Simulates payment gateway interaction (no real money)

Automated documents: PDF invoice generation from order data

Shipment tracking: Manually updated shipping statuses visible to buyers

Analytics dashboard: Simple charts for suppliers and buyers

Responsive design: Works on mobile and desktop (Tailwind CSS)

Security basics: Password hashing, CSRF protection, input validation

Tech stack used in the prototype (aligned with your thesis):

Backend: Python + Django 5.x

Frontend: Django templates + Tailwind CSS (CDN) + Alpine.js (lightweight interactivity)

Database: SQLite (easily switchable to PostgreSQL)

PDF generation: xhtml2pdf (or weasyprint)

Charts: Chart.js (via CDN)



Final Setup and Running
After copying all files, run these commands in the terminal (inside the project folder with the virtual environment activated):

bash
python manage.py makemigrations marketplace
python manage.py migrate
python manage.py createsuperuser   # follow prompts to create an admin user
python manage.py runserver
Visit http://127.0.0.1:8000/. You can:

Register a supplier and a buyer.

Add categories via the admin interface (/admin) first – create a few categories like "Dresses", "Shirts", "Jeans", "Children's Wear". You can also create subcategories by setting a parent.

Supplier: add products with images, prices, and grades.

Buyer: browse, add to cart, checkout, simulate payment, download invoice, track shipment.

Note for images: The media folder will be created automatically. In development, Django serves media files only when DEBUG=True.

This fully functional prototype aligns perfectly with your project's described system. It demonstrates all the core workflows: user roles, product listing, order management, mock payment, document generation, and basic analytics. You can now present this as a proof-of-concept alongside your thesis



Now test the platform
Start the server: python manage.py runserver

Visit http://127.0.0.1:8000/login/ and log in as:

Buyer: username buyer1, password buyer123
(You’ll see the sample products on the Marketplace page)

Supplier: username supplier1, password supplier123
(You’ll see your listed products on the dashboard)

You can also add more products via the supplier’s “Add Product” page