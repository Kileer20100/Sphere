import sphere_native_rust
def vendor() -> str:
    return sphere_native_rust.vendor()

def brand() -> str:
    return sphere_native_rust.brand()

def logical_cores() -> int:
    return sphere_native_rust.logical_cores()

def physical_cores() -> int:
    return sphere_native_rust.physical_cores()

def cpu_frequency_mhz() -> int:
    return sphere_native_rust.cpu_frequency_mhz()

def cpu_family() -> int:
    return sphere_native_rust.cpu_family()

def cpu_model() -> int:
    return sphere_native_rust.cpu_model()

def cpu_stepping() -> int:
    return sphere_native_rust.cpu_stepping()

def architecture() -> str:
    return sphere_native_rust.architecture()

def l1_cache_size_kb() -> int:
    return sphere_native_rust.l1_cache_size_kb()

def l2_cache_size_kb() -> int:
    return sphere_native_rust.l2_cache_size_kb()

def l3_cache_size_kb() -> int:
    return sphere_native_rust.l3_cache_size_kb()

def hyperthreading() -> bool:
    return sphere_native_rust.hyperthreading()

def virtualization() -> bool:
    return sphere_native_rust.has_virtualization()

def has_fpu() -> bool:
    return sphere_native_rust.has_fpu()

def has_mmx() -> bool:
    return sphere_native_rust.has_mmx()

def has_sse() -> bool:
    return sphere_native_rust.has_sse()

def has_sse2() -> bool:
    return sphere_native_rust.has_sse2()

def has_sse3() -> bool:
    return sphere_native_rust.has_sse3()

def has_ssse3() -> bool:
    return sphere_native_rust.has_ssse3()

def has_sse4_1() -> bool:
    return sphere_native_rust.has_sse4_1()

def has_sse4_2() -> bool:
    return sphere_native_rust.has_sse4_2()

def has_avx() -> bool:
    return sphere_native_rust.has_avx()

def has_avx2() -> bool:
    return sphere_native_rust.has_avx2()

def has_fma() -> bool:
    return sphere_native_rust.has_fma()

def has_aes() -> bool:
    return sphere_native_rust.has_aes()

def has_rdrand() -> bool:
    return sphere_native_rust.has_rdrand()

def has_bmi1() -> bool:
    return sphere_native_rust.has_bmi1()

def has_bmi2() -> bool:
    return sphere_native_rust.has_bmi2()