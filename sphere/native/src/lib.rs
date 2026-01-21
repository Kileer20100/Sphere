use pyo3::prelude::*;

#[pyfunction]
fn cpu_count() -> usize {
    32
}

#[pymodule]
fn sphere_native_rust(_py: Python, m: &PyModule) -> PyResult<()>{
    m.add_function(wrap_pyfunction!(cpu_count, m)?)?;
    Ok(())
}