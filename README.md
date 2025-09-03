# Local Embedding Server (OpenAI-compatible)

A FastAPI-based server that provides text embeddings using the INSTRUCTOR-large model, offering an OpenAI-compatible API interface.

## Features

- OpenAI-compatible API endpoint for text embeddings
- Uses the powerful INSTRUCTOR-large model
- Support for both single text and batch text embedding generation
- Token usage tracking
- REST API with FastAPI

## Prerequisites

- Docker, Docker Compose
- Sufficient disk space for the model (approximately 5GB)
- Stable internet connection (for initial model download)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Ercogx/embedding-server && cd embedding-server 
```

2. Run docker
```bash
docker compose up -d 
```

### API Endpoints

#### POST /v1/embeddings

Generate embeddings for given text(s).

**Request Body:**
```json
{
    "model": "instructor-large",
    "input": "string or array of strings"
}
```

#### Response

```json
{
    "object": "list",
    "data": [
        {
            "object": "embedding",
            "embedding": [float],
            "index": integer
        }
    ],
    "model": "instructor-large",
    "usage": {
        "prompt_tokens": integer,
        "total_tokens": integer
    }
}
```

## Error Handling

The server provides appropriate error messages for common issues:

- 400: Invalid model specified
- 503: Model not initialized
- 500: Internal server error during embedding generation

## License

The project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).

## Contributing 🤝
We welcome contributions!