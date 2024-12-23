# Use the Node.js image
FROM node:22
# Set the working directory
WORKDIR /app
# Copy the package.json and install dependencies
COPY package.json .
RUN npm install
# Copy the rest of the frontend code
COPY . .
# Expose the port the frontend runs on
EXPOSE 3000
# Command to run the frontend server
CMD ["npm", "run", "dev"]
