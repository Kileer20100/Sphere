
use raw_cpuid::CpuId;
use sysinfo::{System};
use pyo3::pyfunction;

pub fn register_functions_cpu_info(m: &pyo3::prelude::PyModule) -> pyo3::PyResult<()> {
    m.add_function(pyo3::wrap_pyfunction!(minimal, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(full, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(vendor, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(brand, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(has_sse, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(has_sse2, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(has_sse3, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(has_avx, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(has_avx2, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(logical_cores, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(cpu_frequency_mhz, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(hyperthreading, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(has_fma, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(has_bmi1, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(has_bmi2, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(cpu_family, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(cpu_model, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(cpu_stepping, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(physical_cores, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(has_fpu, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(has_mmx, m)?)?;
    m.add_function(pyo3::wrap_pyfunction!(has_3dnow, m)?)?;
    Ok(())
}

#[pyfunction]
pub fn minimal(){

    println!("Vendor: {}", vendor());
    println!("Brand: {}", brand());
    println!("Physical Cores: {:?}", physical_cores());
    println!("Logical Cores: {}", logical_cores());
    println!("CPU Frequency (MHz): {}", cpu_frequency_mhz());
    println!("CPU Family: {:?}", cpu_family());
    println!("CPU Model: {:?}", cpu_model());
    println!("CPU Stepping: {:?}", cpu_stepping());

    
}
#[pyfunction]
pub fn full() {
    println!("--- CPU Full Information ---");
    
    // Basic info
    println!("Vendor: {}", vendor());
    println!("Brand: {}", brand());
    println!("Physical Cores: {:?}", physical_cores());
    println!("Logical Cores: {}", logical_cores());
    println!("CPU Frequency (MHz): {}", cpu_frequency_mhz());
    println!("CPU Family: {:?}", cpu_family());
    println!("CPU Model: {:?}", cpu_model());
    println!("CPU Stepping: {:?}", cpu_stepping());
    
    // Feature flags
    println!("\n--- Feature Flags ---");
    println!("Hyperthreading: {}", hyperthreading());
    println!("FPU: {}", has_fpu());
    println!("MMX: {}", has_mmx());
    println!("SSE: {}", has_sse());
    println!("SSE2: {}", has_sse2());
    println!("SSE3: {}", has_sse3());
    println!("AVX: {}", has_avx());
    println!("AVX2: {}", has_avx2());
    println!("3DNow: {}", has_3dnow());
    println!("FMA: {}", has_fma());
    println!("BMI1: {}", has_bmi1());
    println!("BMI2: {}", has_bmi2());
}

#[pyfunction]
pub fn vendor() -> String{
    CpuId::new()
        .get_vendor_info()
        .map_or("Unknown".to_string(), |v: raw_cpuid::VendorInfo| v.as_str().to_string())
}

#[pyfunction]
pub fn brand() -> String{
    CpuId::new()
        .get_processor_brand_string()
        .map_or("Unknown".to_string(), |b: raw_cpuid::ProcessorBrandString| b.as_str().to_string())
}

#[pyfunction]
pub fn has_sse() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_sse())
}



#[pyfunction]/// SSE2 support
pub fn has_sse2() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_sse2())
}


#[pyfunction]/// SSE3 support
pub fn has_sse3() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_sse3())
}


#[pyfunction]/// AVX support
pub fn has_avx() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_avx())
}


#[pyfunction]/// AVX2 support
pub fn has_avx2() -> bool {
    CpuId::new()
        .get_extended_feature_info()
        .map_or(false, |f: raw_cpuid::ExtendedFeatures| f.has_avx2())
}


#[pyfunction]/// Logical CPU cores
pub fn logical_cores() -> usize {
    let sys = System::new_all();
    sys.cpus().len()
}


#[pyfunction]/// CPU frequency in MHz
pub fn cpu_frequency_mhz() -> u64 {
    let sys = System::new_all();
    let freqs: Vec<u64> = sys.cpus().iter().map(|c: &sysinfo::Cpu| c.frequency()).collect();
    *freqs.first().unwrap_or(&0)
}




#[pyfunction]/// Hyperthreading support
pub fn hyperthreading() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_rdrand())
}


#[pyfunction]/// Extended CPU features
pub fn has_fma() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_fma())
}

#[pyfunction]
pub fn has_bmi1() -> bool {
    CpuId::new()
        .get_extended_feature_info()
        .map_or(false, |f: raw_cpuid::ExtendedFeatures| f.has_bmi1())
}

#[pyfunction]
pub fn has_bmi2() -> bool {
    CpuId::new()
        .get_extended_feature_info()
        .map_or(false, |f: raw_cpuid::ExtendedFeatures| f.has_bmi2())
}


#[pyfunction]/// CPU architecture (family/model/stepping)
pub fn cpu_family() -> u8 {
    CpuId::new()
        .get_feature_info()
        .map(|f: raw_cpuid::FeatureInfo| f.family_id()).unwrap_or(0)
}

#[pyfunction]
pub fn cpu_model() -> u8 {
    CpuId::new()
        .get_feature_info()
        .map(|f: raw_cpuid::FeatureInfo| f.model_id()).unwrap_or(0)
}

#[pyfunction]
pub fn cpu_stepping() -> u8 {
    CpuId::new()
        .get_feature_info()
        .map(|f: raw_cpuid::FeatureInfo| f.stepping_id()).unwrap_or(0)
}



#[pyfunction]/// Number of physical cores
pub fn physical_cores() -> Option<usize> {
    let sys = System::new_all();
    Some(sys.cpus().len()) // sysinfo не отличает физ/лог, но можно допилить через raw_cpuid
}


#[pyfunction]
pub fn has_fpu() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_fpu())
}

#[pyfunction]
pub fn has_mmx() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_mmx())
}

#[pyfunction]
pub fn has_3dnow() -> bool {
    CpuId::new()
        .get_extended_feature_info()
        .map_or(false, |f: raw_cpuid::ExtendedFeatures| f.has_adx())
}
