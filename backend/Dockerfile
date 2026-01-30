FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install production dependencies only
RUN npm ci --only=production

# Copy application code
COPY server.js ./

# Expose the backend port
EXPOSE 3004

# Set default environment variables
ENV NODE_ENV=production
ENV PORT=3004

# Start the server
CMD ["node", "server.js"]
