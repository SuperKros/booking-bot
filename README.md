# Telegram Bot for Booking System

This is a Telegram bot designed to help users book services, manage their appointments, and cancel them. The bot is built using Python and the Aiogram library.

## Features

- **Booking**: Users can book a service by selecting a date and time.
- **View Appointments**: Users can view a list of their booked appointments.
- **Cancel Appointments**: Users can cancel any of their existing appointments.
- **Multi-language Support**: The bot supports both English and Ukrainian.

## Technologies

- Python 3.12
- Aiogram
- SQLite (for storing bookings)
- GitHub (for version control)

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/booking-bot.git
Create a virtual environment:

bash
python -m venv venv
Install dependencies:

bash
pip install -r requirements.txt
Add your bot token to the bot.py file:

python
TOKEN = "your-bot-token"
Run the bot:

bash
python bot.py

Commands
/start - Starts the bot and shows a welcome message with available options.
Booking: Tap 📅 Записатися to book a service.
View Appointments: Tap 📝 Мої записи to see your bookings.
Cancel Appointment: Tap ❌ Скасувати [ID] to cancel an appointment.

