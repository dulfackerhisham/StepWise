# StepWise E-Commerce Website
StepWise is your go-to destination for a seamless online shopping experience! 🛍️

StepWise leverages the power of Python Django for robust server-side functionalities and PostgreSQL for secure data storage. With a focus on security and efficiency, our platform combines advanced features to make your shopping journey enjoyable and secure.

## Key Features
**User Verification:** We prioritize your security with OTP-based verification for user accounts.

**Integrated Payment:** Complete your purchases effortlessly with Razorpay, a trusted and efficient payment gateway.

**AWS Deployment:** StepWise is proudly deployed on AWS EC2 for scalability and reliability, utilizing NGINX and Unicorn for optimal performance.

**Bulk Create and Efficiency:**
StepWise optimizes performance by utilizing Django's `bulk_create` for efficient database operations. This ensures quick and reliable handling of a large number of database inserts.

**Locking Mechanism:**
Our platform incorporates a robust locking mechanism to manage product quantities accurately. This prevents any race conditions, offering a smooth shopping experience even in a multi-user environment.

**Asynchronous Task Processing with Celery:**
StepWise leverages Celery for asynchronous task processing. Time-consuming tasks, such as sending order confirmation emails, are handled asynchronously, enhancing the overall responsiveness of the application.

## Technologies Used

StepWise harnesses a powerful stack of technologies to deliver a cutting-edge E-commerce experience:

- **Python Django:** The foundation of StepWise, providing a solid server-side framework.
- **PostgreSQL:** Our database choice, ensuring secure and efficient data management.
- **Ajax:** Enhancing interactivity and responsiveness for a smoother user experience.
- **Celery:** Enabling asynchronous task processing for improved performance.
- **Bootstrap:** Crafting a sleek and responsive design for an enhanced user interface.
- **Razorpay:** Seamless payment integration for quick and hassle-free transactions.
- **Unicorn:** A high-performance HTTP server for deployment, contributing to the website's speed and reliability.
- **Nginx:** Powering our deployment with NGINX to optimize performance and handle incoming traffic efficiently.
- **AWS:** Hosted on AWS EC2 for scalability and availability.
