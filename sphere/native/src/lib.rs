use pyo3::prelude::*;


mod cpu_info;
#[pymodule]
fn sphere_native_rust(_py: Python, m: &PyModule) -> PyResult<()>{
    cpu_info::register_functions_cpu_info(m)?;
    Ok(())
}