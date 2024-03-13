# Use the official Python base image for Windows
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Set working directory
WORKDIR /app

# Install Python and pip
RUN powershell -Command \
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe -OutFile python-3.9.5-amd64.exe; \
    Start-Process python-3.9.5-amd64.exe -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait; \
    Remove-Item python-3.9.5-amd64.exe; \
    pip install --upgrade pip

# Install OpenAI, python-dotenv, and Redis
RUN pip install openai python-dotenv redis

# Set environment variable for OpenAI API key
ENV OPENAI_API_KEY=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

# Copy the install.bat script from the host to the container
COPY install.bat .

# Run the install.bat script
CMD ["cmd", "/c", "install.bat"]
