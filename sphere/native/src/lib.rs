use pyo3::prelude::*;


mod cpu_info;
mod gpu_info;
#[pymodule]
fn sphere_native_rust(_py: Python, m: &PyModule) -> PyResult<()>{
    cpu_info::register_functions_cpu_info(m)?;
    gpu_info::register_functions_gpu_info(m)?;
    Ok(())
}