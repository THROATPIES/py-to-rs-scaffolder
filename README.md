# Python to Rust (Functionality tool for Dirt-CLI Builder)

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Developing a way to scaffold a Dirt-CLI project with python as our bootstrapper.

## Getting Started <a name = "getting_started"></a>

In the main.py youll find 
# Create a new Rust binary project with dependencies
project_name = "my_rust_binary"
project_type = "bin"
dependencies = ["serde", "tokio"]
rust_project = RustProject(project_name, project_type, dependencies)
rust_project.create_project()

# Write Rust code to the binary project
rust_code = """
fn main() {
    println!("Hello, world!");
}
"""
rust_project.write_code(rust_code)

# Build and run the Rust binary code
rust_project.build_and_run()

# If you want to clean up the Rust project, uncomment the following line:
# rust_project.cleanup()


### Prerequisites

What things you need to install the software and how to install them.

```
Python
Rust
Cargo-Edit
```
