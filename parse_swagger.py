#!/usr/bin/env python3
import json
import os
import sys
import re

# Function to convert a path endpoint to markdown
def endpoint_to_markdown(path, path_data):
    markdown = []
    for method, method_data in path_data.items():
        if method in ['get', 'post', 'put', 'delete', 'patch']:
            # Create heading with method and path
            markdown.append(f"### {method.upper()} {path}")
            
            # Add summary and description
            if 'summary' in method_data:
                markdown.append(f"\n**Summary:** {method_data['summary']}")
            
            if 'description' in method_data:
                description = method_data['description'].replace("<br />", "\n").replace("<br>", "\n")
                description = description.replace("<B>", "**").replace("</B>", "**")
                description = description.replace("<b>", "**").replace("</b>", "**")
                description = description.replace("<i>", "*").replace("</i>", "*")
                # Remove HTML tags
                description = description.replace("<ul>", "").replace("</ul>", "")
                description = description.replace("<li>", "- ").replace("</li>", "")
                description = description.replace("<ol>", "").replace("</ol>", "")
                description = re.sub(r'<a[^>]*>|</a>', '', description)  # Remove all a tags
                description = re.sub(r'<span[^>]*>|</span>', '', description)  # Remove span tags
                description = re.sub(r'<p[^>]*>|</p>', '\n', description)  # Replace p tags with newlines
                description = re.sub(r'<H[0-9][^>]*>|</H[0-9]>', '', description)  # Remove H tags
                description = re.sub(r'<pre>|</pre>', '```\n', description)  # Convert pre tags to markdown code blocks
                
                markdown.append(f"\n**Description:** {description}")
            
            # Add parameters
            if 'parameters' in method_data and method_data['parameters']:
                markdown.append("\n**Parameters:**")
                for param in method_data['parameters']:
                    required = " (Required)" if 'required' in param and param['required'] else ""
                    param_type = f"Type: {param['type']}" if 'type' in param else "Type: object"
                    param_desc = f"Description: {param['description']}" if 'description' in param else ""
                    markdown.append(f"- `{param['name']}`{required}: {param_type}. {param_desc}")
            
            # Add responses
            if 'responses' in method_data and method_data['responses']:
                markdown.append("\n**Responses:**")
                for status_code, response_data in method_data['responses'].items():
                    desc = response_data.get('description', '')
                    markdown.append(f"- **{status_code}**: {desc}")
            
            markdown.append("\n---\n")
    
    return "\n".join(markdown)

def generate_toc(tags):
    toc = ["# Table of Contents\n"]
    toc.append("1. [Introduction](#introduction)")
    toc.append("2. [Authentication](#authentication)")
    toc.append("3. [API Usage Guide](#api-usage-guide)")
    toc.append("4. [Error Handling](#error-handling)")
    toc.append("5. [API Endpoints](#api-endpoints)\n")
    
    for i, tag in enumerate(sorted(tags), 1):
        # Create a link-friendly version of the tag
        tag_link = tag.lower().replace(' ', '-')
        toc.append(f"   {i}. [{tag}](#{tag_link})")
    
    return "\n".join(toc)

def api_usage_guide():
    return """
## API Usage Guide

### Base URL
The base URL for all API requests is: `https://[your-mobicontrol-server]/MobiControl/api`

### Authentication
Before making API calls, you need to obtain an OAuth2 access token:

1. **Request an access token**:
   ```
   POST /token
   Authorization: Basic {base64 encoded client_id:client_secret}
   Content-Type: application/x-www-form-urlencoded
   
   grant_type=password&username={admin_username}&password={admin_password}
   ```

2. **Use the access token**:
   ```
   GET /devices
   Authorization: Bearer {access_token}
   ```

### Making Requests
- All requests should include the `Authorization` header with your access token
- For POST and PUT requests, include `Content-Type: application/json` header
- Request and response bodies use JSON format

### Pagination
Many endpoints that return lists support pagination using the following parameters:
- `skip`: Number of items to skip
- `take`: Number of items to retrieve

### Filtering and Sorting
- Use the `filter` parameter to filter results (format: `Property1:Value1,Property2:Value2`)
- Use the `order` parameter to sort results (prefix with + for ascending, - for descending)

## Error Handling

MobiControl uses standard HTTP response codes:
- `2xx`: Success
- `4xx`: Client error (invalid input, authentication issues)
- `5xx`: Server error

Common error codes:
- `400`: Contract validation error (invalid input)
- `401/403`: Authentication/authorization error
- `422`: Business logic error
- `500`: Server error

Error responses include additional information in the response body to help identify the issue.
"""

def main():
    try:
        # Open the Swagger file
        with open('swagger.json', 'r', encoding='utf-8') as f:
            swagger = json.load(f)
        
        # Create Markdown file with basic structure
        with open('MobiControl_API_Documentation.md', 'w', encoding='utf-8') as f:
            # Write header
            f.write("# SOTI MobiControl API Documentation\n\n")
            
            # Extract all tags for TOC
            all_tags = set()
            for path, path_data in swagger['paths'].items():
                for method, method_data in path_data.items():
                    if method in ['get', 'post', 'put', 'delete', 'patch']:
                        tags = method_data.get('tags', ['Other'])
                        for tag in tags:
                            all_tags.add(tag)
            
            # Generate and write TOC
            f.write(generate_toc(all_tags))
            f.write("\n\n")
            
            # Write introduction
            f.write("## Introduction\n")
            if 'info' in swagger and 'description' in swagger['info']:
                # Clean up HTML content
                description = swagger['info']['description'].replace("<br>", "\n").replace("<br />", "\n")
                description = description.replace("<B>", "**").replace("</B>", "**")
                description = description.replace("<b>", "**").replace("</b>", "**")
                description = description.replace("<i>", "*").replace("</i>", "*")
                # Remove HTML tags
                description = description.replace("<ul>", "").replace("</ul>", "")
                description = description.replace("<li>", "- ").replace("</li>", "")
                description = description.replace("<ol>", "").replace("</ol>", "")
                description = re.sub(r'<a[^>]*>|</a>', '', description)  # Remove all a tags
                description = re.sub(r'<span[^>]*>|</span>', '', description)  # Remove span tags
                description = re.sub(r'<p[^>]*>|</p>', '\n', description)  # Replace p tags with newlines
                description = re.sub(r'<H[0-9][^>]*>|</H[0-9]>', '', description)  # Remove H tags
                description = re.sub(r'<pre>|</pre>', '```\n', description)  # Convert pre tags to markdown code blocks
                
                f.write(description)
            else:
                f.write("This documentation provides detailed information about the MobiControl REST API.\n")
            
            # Write authentication section
            f.write("\n\n## Authentication\n")
            f.write("MobiControl API calls are protected by OAuth2 (RFC 6749), and support both Resource Owner and Authorization Code grant types.\n")
            
            # Write API usage guide
            f.write(api_usage_guide())
            
            # Write API endpoints
            f.write("\n\n## API Endpoints\n\n")
            
            # Group endpoints by tags
            endpoints_by_tag = {}
            
            for path, path_data in swagger['paths'].items():
                for method, method_data in path_data.items():
                    if method in ['get', 'post', 'put', 'delete', 'patch']:
                        tags = method_data.get('tags', ['Other'])
                        for tag in tags:
                            if tag not in endpoints_by_tag:
                                endpoints_by_tag[tag] = []
                            endpoints_by_tag[tag].append((path, path_data))
                            break  # Only use the first tag
            
            # Write endpoints grouped by tag
            for tag, endpoints in sorted(endpoints_by_tag.items()):
                f.write(f"## {tag}\n\n")
                
                # Remove duplicates (same path, different methods)
                unique_endpoints = []
                unique_paths = set()
                for path, path_data in endpoints:
                    if path not in unique_paths:
                        unique_paths.add(path)
                        unique_endpoints.append((path, path_data))
                
                # Write each endpoint
                for path, path_data in unique_endpoints:
                    f.write(endpoint_to_markdown(path, path_data))
        
        print("Documentation generated successfully: MobiControl_API_Documentation.md")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 