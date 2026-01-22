
use raw_cpuid::CpuId;
use sysinfo::{System};
use pyo3::pyfunction;

pub fn register_functions_cpu_info(m: &pyo3::prelude::PyModule) -> pyo3::PyResult<()> {
    // Basic information functions
    m.add_function(wrap_pyfunction!(py_vendor, m)?)?;
    m.add_function(wrap_pyfunction!(py_brand, m)?)?;
    m.add_function(wrap_pyfunction!(py_logical_cores, m)?)?;
    m.add_function(wrap_pyfunction!(py_physical_cores, m)?)?;
    m.add_function(wrap_pyfunction!(py_cpu_frequency_mhz, m)?)?;
    
    // CPU architecture
    m.add_function(wrap_pyfunction!(py_cpu_family, m)?)?;
    m.add_function(wrap_pyfunction!(py_cpu_model, m)?)?;
    m.add_function(wrap_pyfunction!(py_cpu_stepping, m)?)?;
    m.add_function(wrap_pyfunction!(py_architecture, m)?)?;
    
    // Cache information
    m.add_function(wrap_pyfunction!(py_l1_cache_size_kb, m)?)?;
    m.add_function(wrap_pyfunction!(py_l2_cache_size_kb, m)?)?;
    m.add_function(wrap_pyfunction!(py_l3_cache_size_kb, m)?)?;
    
    // Feature flags
    m.add_function(wrap_pyfunction!(py_hyperthreading, m)?)?;
    m.add_function(wrap_pyfunction!(py_virtualization, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_fpu, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_mmx, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_sse, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_sse2, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_sse3, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_ssse3, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_sse4_1, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_sse4_2, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_avx, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_avx2, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_fma, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_aes, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_rdrand, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_bmi1, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_bmi2, m)?)?;
    m.add_function(wrap_pyfunction!(py_has_3dnow, m)?)?;
    
    // Convenience functions
    m.add_function(wrap_pyfunction!(py_minimal, m)?)?;
    m.add_function(wrap_pyfunction!(py_full, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_all_info, m)?)?;
    
    Ok(())
}


#[pyfunction]
pub fn minimal(){
    println!("--- CPU Minimal Information ---");
    println!("Vendor: {}", vendor());
    println!("Brand: {}", brand());
    println!("Physical Cores: {:?}", physical_cores());
    println!("CPU Frequency (MHz): {}", cpu_frequency_mhz());
    println!("Architecture: {}", architecture());
    println!();

    
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
    println!("Architecture: {}", architecture());
    
    // Cache info
    println!("\n--- Cache Information ---");
    println!("L1 Cache: {} KB", l1_cache_size_kb());
    println!("L2 Cache: {} KB", l2_cache_size_kb());
    println!("L3 Cache: {} KB", l3_cache_size_kb());
    
    // Feature flags
    println!("\n--- Feature Flags ---");
    println!("Hyperthreading: {}", hyperthreading());
    println!("Virtualization: {}", has_virtualization());
    println!("FPU: {}", has_fpu());
    println!("MMX: {}", has_mmx());
    println!("SSE: {}", has_sse());
    println!("SSE2: {}", has_sse2());
    println!("SSE3: {}", has_sse3());
    println!("SSSE3: {}", has_ssse3());
    println!("SSE4.1: {}", has_sse4_1());
    println!("SSE4.2: {}", has_sse4_2());
    println!("AVX: {}", has_avx());
    println!("AVX2: {}", has_avx2());
    println!("FMA: {}", has_fma());
    println!("AES-NI: {}", has_aes());
    println!("RDRAND: {}", has_rdrand());
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
pub fn hyperthreading() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_htt())
}


use std::fs;
#[pyfunction]
pub fn l1_cache_size_kb() -> u32 {
    match get_cache_size_for_level(1) {
        Some(size) => size,
        None => 0
    }
}
#[pyfunction]
pub fn l2_cache_size_kb() -> u32 {
    match get_cache_size_for_level(2) {
        Some(size) => size,
        None => 0
    }
}
#[pyfunction]
pub fn l3_cache_size_kb() -> u32 {
    match get_cache_size_for_level(3) {
        Some(size) => size,
        None => 0
    }
}

fn get_cache_size_for_level(level: u8) -> Option<u32> {
    let cache_dir = "/sys/devices/system/cpu/cpu0/cache";
    
    if let Ok(entries) = fs::read_dir(cache_dir) {
        for entry in entries.flatten() {
            let path = entry.path();
            let index_path = path.join("level");
            let size_path = path.join("size");
            
            if let (Ok(lvl_str), Ok(size_str)) = (
                fs::read_to_string(&index_path),
                fs::read_to_string(&size_path)
            ) {
                if lvl_str.trim() == level.to_string() {
                    return parse_cache_size_kb(&size_str);
                }
            }
        }
    }
    
    None
}

fn parse_cache_size_kb(size_str: &str) -> Option<u32> {
    let trimmed = size_str.trim();
    if trimmed.is_empty() {
        return None;
    }
    
    let last_char = trimmed.chars().last().unwrap();
    
    // Если последний символ буква (K, M, G)
    if last_char.is_alphabetic() {
        let num_part = &trimmed[..trimmed.len()-1];
        let num: u32 = num_part.parse().unwrap_or(0);
        
        match last_char {
            'K' => Some(num),
            'M' => Some(num * 1024),
            'G' => Some(num * 1024 * 1024),
            _ => Some(num),
        }
    } else {
        // Если нет суффикса, просто парсим число
        trimmed.parse().ok()
    }
}

#[pyfunction]/// Поддержка виртуализации
pub fn has_virtualization() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f| f.has_vmx())
}


#[pyfunction]/// AES инструкции
pub fn has_aes() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_aesni())
}

#[pyfunction]/// SSE4.1
pub fn has_sse4_1() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_sse41())
}

#[pyfunction]/// SSE4.2
pub fn has_sse4_2() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_sse42())
}

#[pyfunction]/// SSSE3
pub fn has_ssse3() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_ssse3())
}

#[pyfunction]/// Поддержка RDRAND
pub fn has_rdrand() -> bool {
    CpuId::new()
        .get_feature_info()
        .map_or(false, |f: raw_cpuid::FeatureInfo| f.has_rdrand())
}


#[pyfunction]/// Определение архитектуры
pub fn architecture() -> String {
    let vendor = vendor();
    if vendor.contains("Intel") {
        "x86_64 (Intel)".to_string()
    } else if vendor.contains("AMD") {
        "x86_64 (AMD)".to_string()
    } else if vendor.contains("ARM") {
        "ARM".to_string()
    } else {
        "Unknown".to_string()
    }
}

#[pyfunction]
pub fn physical_cores() -> usize {
    // Читаем из /proc/cpuinfo
    if let Ok(content) = fs::read_to_string("/proc/cpuinfo") {
        for line in content.lines() {
            if line.starts_with("cpu cores") {
                if let Some(value) = line.split(':').nth(1) {
                    if let Ok(cores) = value.trim().parse::<usize>() {
                        return cores;
                    }
                }
            }
        }
    }
    
    // Fallback
    logical_cores()
}
