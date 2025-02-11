# Email Sender Script

This project is a simple Python script for sending emails to multiple recipients from a Gmail account. It reads recipient addresses from a text file, composes an email, and sends it to each recipient while maintaining a delay between each message to avoid spam detection.

## Features
- Reads email addresses from a text file (`emails.txt`).
- Sends personalized emails to multiple recipients.
- Configurable delay between emails (default: 10 seconds).
- Uses environment variables for secure management of email credentials.

## Prerequisites
- **Python 3.x**
- **A Gmail account**
- **`dotenv` library for environment variable management**

### Install Required Python Libraries
```bash
pip install python-dotenv
```

## Setup
1. Clone this repository.
   ```bash
   git clone https://github.com/yourusername/EmailSender.git
   cd EmailSender
   ```
2. Create a file named `.env` in the project directory and add the following environment variables:
   ```env
   EMAIL_SENDER=your_email@gmail.com
   EMAIL_PASSWORD=your_email_password_or_app_password
   ```
   > **Note:** For security reasons, it’s recommended to use an [App Password](https://support.google.com/accounts/answer/185833?hl=en) instead of your main Gmail password.

3. Create a file named `emails.txt` in the project directory and list the recipient email addresses, one per line.

4. Run the script:
   ```bash
   python EmailSender.py
   ```

## Script Explanation
### Functions
- **`ler_emails_de_arquivo(caminho_arquivo)`**: Reads recipient email addresses from the specified file.
- **`enviar_email(remetente, senha, destinatario, assunto, mensagem)`**: Handles the composition and sending of the email.
- **`main()`**: Coordinates reading emails, composing the message, and sending it to each recipient with a delay.

### Configuration
- **Subject:** `Email Sender`
- **Default Message:**
  ```plaintext
  Hello,

  I hope this email finds you well.

  Best regards.
  ```

## Important Notes
- **Email Blocking:** Gmail may block your account temporarily if it detects unusual activity. A 10-second delay between emails is added to reduce this risk.
- **Sensitive Data:** Never share your `.env` file or hardcode sensitive information into your code.
- **Message Personalization:** Currently, the message is static. Consider extending the script to personalize the message for each recipient.

## License
This project is licensed under the MIT License.

