import typer
import psutil
from ...lib.cpu import vendor, brand, logical_cores, physical_cores, cpu_frequency_mhz, cpu_family, cpu_model, cpu_stepping, architecture, l1_cache_size_kb, l2_cache_size_kb, l3_cache_size_kb, hyperthreading, virtualization, has_fpu, has_mmx, has_sse, has_sse2, has_sse3, has_ssse3, has_sse4_1, has_sse4_2, has_avx, has_avx2, has_fma, has_aes, has_rdrand, has_bmi1, has_bmi2


def minimal():
    """Minimal CPU info with colors"""
    typer.echo()
    typer.echo(typer.style("=== MINIMAL CPU INFORMATION ===", 
                          fg=typer.colors.GREEN, bold=True))
    typer.echo()
    
    typer.echo(
        typer.style("Vendor: ", fg=typer.colors.CYAN, bold=True) +
        typer.style(vendor(), fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("Brand: ", fg=typer.colors.CYAN, bold=True) +
        typer.style(brand(), fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("Architecture: ", fg=typer.colors.CYAN, bold=True) +
        typer.style(architecture(), fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("Cores: ", fg=typer.colors.CYAN, bold=True) +
        typer.style(f"{physical_cores()}P / {logical_cores()}L", 
                   fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("Frequency: ", fg=typer.colors.MAGENTA, bold=True) +
        typer.style(f"{cpu_frequency_mhz()} MHz", fg=typer.colors.WHITE)
    )
    
    # Cache summary
    typer.echo(
        typer.style("Cache: ", fg=typer.colors.MAGENTA, bold=True) +
        typer.style(f"L1={l1_cache_size_kb()}K ", fg=typer.colors.WHITE) +
        typer.style(f"L2={l2_cache_size_kb()}K ", fg=typer.colors.WHITE) +
        typer.style(f"L3={l3_cache_size_kb()}K", fg=typer.colors.WHITE)
    )
    
    typer.echo()

def full():
    """Full CPU info with colored booleans"""
    typer.echo()
    typer.echo(typer.style("=== FULL CPU INFORMATION ===", 
                          fg=typer.colors.GREEN, bold=True))
    typer.echo()
    
    # ===== Basic Information =====
    typer.echo(typer.style("--- Basic Information ---", 
                          fg=typer.colors.CYAN, bold=True))
    
    typer.echo(
        typer.style("Vendor: ", fg=typer.colors.CYAN) +
        typer.style(vendor(), fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("Brand: ", fg=typer.colors.CYAN) +
        typer.style(brand(), fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("Architecture: ", fg=typer.colors.CYAN) +
        typer.style(architecture(), fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("Physical Cores: ", fg=typer.colors.CYAN) +
        typer.style(str(physical_cores()), fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("Logical Cores: ", fg=typer.colors.CYAN) +
        typer.style(str(logical_cores()), fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("CPU Frequency: ", fg=typer.colors.MAGENTA) +
        typer.style(f"{cpu_frequency_mhz()} MHz", fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("CPU Family: ", fg=typer.colors.YELLOW) +
        typer.style(str(cpu_family()), fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("CPU Model: ", fg=typer.colors.YELLOW) +
        typer.style(str(cpu_model()), fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("CPU Stepping: ", fg=typer.colors.YELLOW) +
        typer.style(str(cpu_stepping()), fg=typer.colors.WHITE)
    )
    
    typer.echo()
    
    # ===== Cache Information =====
    typer.echo(typer.style("--- Cache Information ---", 
                          fg=typer.colors.MAGENTA, bold=True))
    
    typer.echo(
        typer.style("L1 Cache: ", fg=typer.colors.MAGENTA) +
        typer.style(f"{l1_cache_size_kb()} KB", fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("L2 Cache: ", fg=typer.colors.MAGENTA) +
        typer.style(f"{l2_cache_size_kb()} KB", fg=typer.colors.WHITE)
    )
    
    typer.echo(
        typer.style("L3 Cache: ", fg=typer.colors.MAGENTA) +
        typer.style(f"{l3_cache_size_kb()} KB", fg=typer.colors.WHITE)
    )
    
    typer.echo()
    
    # ===== Feature Flags =====
    typer.echo(typer.style("--- Feature Flags ---", 
                          fg=typer.colors.YELLOW, bold=True))
    
    feature_flags = {
        "Hyperthreading": hyperthreading(),
        "Virtualization": virtualization(),
        "FPU": has_fpu(),
        "MMX": has_mmx(),
        "SSE": has_sse(),
        "SSE2": has_sse2(),
        "SSE3": has_sse3(),
        "SSSE3": has_ssse3(),
        "SSE4.1": has_sse4_1(),
        "SSE4.2": has_sse4_2(),
        "AVX": has_avx(),
        "AVX2": has_avx2(),
        "FMA": has_fma(),
        "AES-NI": has_aes(),
        "RDRAND": has_rdrand(),
        "BMI1": has_bmi1(),
        "BMI2": has_bmi2(),
    }
    
    for feature, supported in feature_flags.items():
        if supported:
            status = typer.style("✓", fg=typer.colors.GREEN, bold=True)
        else:
            status = typer.style("✗", fg=typer.colors.RED, bold=True)
        
        typer.echo(f"  {status} {feature}")
    
    typer.echo()

# ===== CLI функция =====
def cpu_show(mode: str):
    if mode == "minimal":
        minimal()
    elif mode == "full":
        full()
    else:
        typer.echo("Please specify a valid mode: '-m' or '-f'.")
