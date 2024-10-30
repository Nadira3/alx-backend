# Caching System Project

This project implements a caching system in which various cache replacement policies are applied to manage stored data. The goal is to understand and demonstrate how different caching strategies work, including FIFO, LIFO, LRU, MRU, and LFU, and to explore the purpose and limitations of a caching system.

## Table of Contents
- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Caching Policies](#caching-policies)
  - [FIFO (First In, First Out)](#fifo-first-in-first-out)
  - [LIFO (Last In, First Out)](#lifo-last-in-first-out)
  - [LRU (Least Recently Used)](#lru-least-recently-used)
  - [MRU (Most Recently Used)](#mru-most-recently-used)
  - [LFU (Least Frequently Used)](#lfu-least-frequently-used)
- [Project Purpose](#project-purpose)
- [Cache Limitations](#cache-limitations)
- [Contributing](#contributing)
- [License](#license)

## About the Project
This caching system demonstrates how different cache replacement algorithms work. It provides insight into how a cache stores, retrieves, and evicts data based on the specific policy in use, making it a valuable learning tool for understanding the efficiency trade-offs between different caching strategies.

## Getting Started

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/) (or language/environment your project uses)
- A code editor like [VS Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/caching-system.git
   cd caching-system
   ```

2. Install required dependencies (if applicable):

```
pip install -r requirements.txt
```

## Usage

1. Run the project with:
```
python main.py
```

2. Specify the caching policy you'd like to test (e.g., FIFO, LRU, etc.).


3. Monitor cache performance, hit/miss rates, and eviction processes based on the selected policy.


## Caching Policies

- FIFO (First In, First Out)

The first item added to the cache is the first one removed when the cache reaches its limit.

- LIFO (Last In, First Out)

The last item added to the cache is the first one removed when the cache reaches its limit.

**LRU** (Least Recently Used)

The item that hasn't been accessed for the longest time is removed when the cache reaches its limit.

**MRU** (Most Recently Used)

The item that was most recently accessed is removed when the cache reaches its limit.

**LFU** (Least Frequently Used)

The item that has been used the least number of times is removed when the cache reaches its limit.

## Project Purpose

The caching system is designed to:

Improve data access efficiency by storing frequently used data.

Demonstrate various cache replacement strategies.

Explore the advantages and disadvantages of each caching method.


## Cache Limitations

Caching systems face the following limitations:

Memory Constraints: Cache size is often limited, requiring strategic data eviction.

Stale Data: Cached data can become outdated if the source data changes.

Overhead: Cache management can add complexity and processing overhead.

Cache Misses: A cache miss occurs when requested data is not found in the cache, requiring access to slower main storage.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for suggestions or improvements.

License

ALX Backend Curriculum
