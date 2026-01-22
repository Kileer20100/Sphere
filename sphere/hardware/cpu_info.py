import typer
import psutil

import  sphere_native_rust

def cpu_show(mode: str):

    if mode == "minimal":
        minimal()
    elif mode == "full":
        full()
    else:
        typer.echo("Please specify a valid mode: '-m' or '-f'.")


def minimal():
    typer.echo()
    typer.echo(typer.style("Minimal CPU Information:", fg=typer.colors.GREEN, bold=True))

    typer.echo(
        typer.style("Vendor: ", fg=typer.colors.CYAN)
        + typer.style(vendor(), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("Brand: ", fg=typer.colors.CYAN)
        + typer.style(brand(), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("Physical Cores: ", fg=typer.colors.CYAN)
        + typer.style(str(physical_cores()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("Logical Cores: ", fg=typer.colors.CYAN)
        + typer.style(str(logical_cores()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("CPU Frequency (MHz): ", fg=typer.colors.MAGENTA)
        + typer.style(f"{cpu_frequency_mhz()}", fg=typer.colors.WHITE)
    )
    typer.echo()

def full():
    typer.echo()
    typer.echo(typer.style("Full CPU Information:", fg=typer.colors.GREEN, bold=True))

    typer.echo(
        typer.style("Vendor: ", fg=typer.colors.CYAN)
        + typer.style(vendor(), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("Brand: ", fg=typer.colors.CYAN)
        + typer.style(brand(), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("Physical Cores: ", fg=typer.colors.CYAN)
        + typer.style(str(physical_cores()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("Logical Cores: ", fg=typer.colors.CYAN)
        + typer.style(str(logical_cores()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("CPU Frequency (MHz): ", fg=typer.colors.MAGENTA)
        + typer.style(str(cpu_frequency_mhz()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("CPU Family: ", fg=typer.colors.YELLOW)
        + typer.style(str(cpu_family()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("CPU Model: ", fg=typer.colors.YELLOW)
        + typer.style(str(cpu_model()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("CPU Stepping: ", fg=typer.colors.YELLOW)
        + typer.style(str(cpu_stepping()), fg=typer.colors.WHITE)
    )

    typer.echo()

    # ===== Feature Flags =====
    typer.echo(typer.style("Feature Flags", fg=typer.colors.GREEN, bold=True))

    typer.echo(
        typer.style("Hyperthreading: ", fg=typer.colors.CYAN)
        + typer.style(str(hyperthreading()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("FPU: ", fg=typer.colors.CYAN)
        + typer.style(str(has_fpu()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("MMX: ", fg=typer.colors.CYAN)
        + typer.style(str(has_mmx()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("SSE: ", fg=typer.colors.CYAN)
        + typer.style(str(has_sse()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("SSE2: ", fg=typer.colors.CYAN)
        + typer.style(str(has_sse2()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("SSE3: ", fg=typer.colors.CYAN)
        + typer.style(str(has_sse3()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("AVX: ", fg=typer.colors.CYAN)
        + typer.style(str(has_avx()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("AVX2: ", fg=typer.colors.CYAN)
        + typer.style(str(has_avx2()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("3DNow: ", fg=typer.colors.CYAN)
        + typer.style(str(has_3dnow()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("FMA: ", fg=typer.colors.CYAN)
        + typer.style(str(has_fma()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("BMI1: ", fg=typer.colors.CYAN)
        + typer.style(str(has_bmi1()), fg=typer.colors.WHITE)
    )

    typer.echo(
        typer.style("BMI2: ", fg=typer.colors.CYAN)
        + typer.style(str(has_bmi2()), fg=typer.colors.WHITE)
    )
    typer.echo()

# ===== Basic info =====

def vendor() -> str:
    return sphere_native_rust.vendor()


def brand() -> str:
    return sphere_native_rust.brand()


def physical_cores() -> int:
    return sphere_native_rust.physical_cores() or 0


def logical_cores() -> int:
    return sphere_native_rust.logical_cores()


def cpu_frequency_mhz() -> int:
    return sphere_native_rust.cpu_frequency_mhz()


def cpu_family() -> int:
    return sphere_native_rust.cpu_family()


def cpu_model() -> int:
    return sphere_native_rust.cpu_model()


def cpu_stepping() -> int:
    return sphere_native_rust.cpu_stepping()


# ===== Feature flags =====

def hyperthreading() -> bool:
    return sphere_native_rust.hyperthreading()


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


def has_avx() -> bool:
    return sphere_native_rust.has_avx()


def has_avx2() -> bool:
    return sphere_native_rust.has_avx2()


def has_3dnow() -> bool:
    return sphere_native_rust.has_3dnow()


def has_fma() -> bool:
    return sphere_native_rust.has_fma()


def has_bmi1() -> bool:
    return sphere_native_rust.has_bmi1()


def has_bmi2() -> bool:
    return sphere_native_rust.has_bmi2()
