# Create a new Rust binary project with dependencies
from createlib import RustProject


project_name = "test_binary_cli_project"
project_type = "bin"
dependencies = ["serde", "tokio"]
rust_project = RustProject(project_name, project_type, dependencies)
rust_project.create_project()

# Write Rust code to the binary project
rust_code = """
fn main() {
    println!("Blazing Fast Rust!");
}
"""
rust_project.write_code(rust_code)

# Build and run the Rust binary code
rust_project.build_and_run()

# If you want to clean up the Rust project, uncomment the following line:
# rust_project.cleanup()
