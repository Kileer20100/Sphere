import typer
from ...lib.gpu import (
    gpu_name, gpu_backend, gpu_vendor, gpu_device_id, gpu_type, gpu_features,
    max_texture_1d, max_texture_2d, max_texture_3d, max_texture_array_layers,
    max_bind_groups, max_dynamic_uniform_buffers, max_dynamic_storage_buffers,
    max_sampled_textures, max_samplers, max_storage_buffers, max_storage_textures,
    max_uniform_buffers, max_uniform_buffer_size, max_storage_buffer_size,
    min_uniform_buffer_alignment, min_storage_buffer_alignment,
    max_vertex_buffers, max_vertex_attributes, max_vertex_stride,
    max_compute_workgroup_storage, max_compute_workgroup_size_x,
    max_compute_workgroup_size_y, max_compute_workgroup_size_z,
    max_compute_workgroup_size_str, max_compute_workgroups_per_dim,
    supported_texture_compression, supported_shader_features
)

# ===== Minimal GPU info =====
def minimal():
    """Minimal GPU info with colors"""
    typer.echo()
    typer.echo(typer.style("=== MINIMAL GPU INFORMATION ===", fg=typer.colors.GREEN, bold=True))
    typer.echo()
    
    typer.echo(typer.style("Name: ", fg=typer.colors.CYAN, bold=True) + typer.style(gpu_name(), fg=typer.colors.WHITE))
    typer.echo(typer.style("Type: ", fg=typer.colors.CYAN, bold=True) + typer.style(gpu_type(), fg=typer.colors.WHITE))
    typer.echo(typer.style("Vendor ID: ", fg=typer.colors.CYAN, bold=True) + typer.style(str(gpu_vendor()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Device ID: ", fg=typer.colors.CYAN, bold=True) + typer.style(str(gpu_device_id()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Backend: ", fg=typer.colors.MAGENTA, bold=True) + typer.style(gpu_backend(), fg=typer.colors.WHITE))
    typer.echo()

# ===== Full GPU info =====
def full():
    """Full GPU info with detailed limits and features"""
    typer.echo()
    typer.echo(typer.style("=== FULL GPU INFORMATION ===", fg=typer.colors.GREEN, bold=True))
    typer.echo()
    
    # --- Basic Info ---
    typer.echo(typer.style("--- Basic Information ---", fg=typer.colors.CYAN, bold=True))
    typer.echo(typer.style("Name: ", fg=typer.colors.CYAN) + typer.style(gpu_name(), fg=typer.colors.WHITE))
    typer.echo(typer.style("Type: ", fg=typer.colors.CYAN) + typer.style(gpu_type(), fg=typer.colors.WHITE))
    typer.echo(typer.style("Vendor ID: ", fg=typer.colors.CYAN) + typer.style(str(gpu_vendor()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Device ID: ", fg=typer.colors.CYAN) + typer.style(str(gpu_device_id()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Backend: ", fg=typer.colors.MAGENTA) + typer.style(gpu_backend(), fg=typer.colors.WHITE))
    typer.echo(typer.style("Features: ", fg=typer.colors.MAGENTA) + typer.style(gpu_features(), fg=typer.colors.WHITE))
    typer.echo()
    
    # --- Texture Limits ---
    typer.echo(typer.style("--- Texture Limits ---", fg=typer.colors.CYAN, bold=True))
    typer.echo(typer.style("Max 1D: ", fg=typer.colors.CYAN) + typer.style(str(max_texture_1d()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max 2D: ", fg=typer.colors.CYAN) + typer.style(str(max_texture_2d()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max 3D: ", fg=typer.colors.CYAN) + typer.style(str(max_texture_3d()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Array Layers: ", fg=typer.colors.CYAN) + typer.style(str(max_texture_array_layers()), fg=typer.colors.WHITE))
    typer.echo()
    
    # --- Bind Groups & Buffers ---
    typer.echo(typer.style("--- Bind Groups & Buffers ---", fg=typer.colors.MAGENTA, bold=True))
    typer.echo(typer.style("Max Bind Groups: ", fg=typer.colors.MAGENTA) + typer.style(str(max_bind_groups()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Dynamic Uniform Buffers: ", fg=typer.colors.MAGENTA) + typer.style(str(max_dynamic_uniform_buffers()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Dynamic Storage Buffers: ", fg=typer.colors.MAGENTA) + typer.style(str(max_dynamic_storage_buffers()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Sampled Textures: ", fg=typer.colors.MAGENTA) + typer.style(str(max_sampled_textures()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Samplers: ", fg=typer.colors.MAGENTA) + typer.style(str(max_samplers()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Storage Buffers: ", fg=typer.colors.MAGENTA) + typer.style(str(max_storage_buffers()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Storage Textures: ", fg=typer.colors.MAGENTA) + typer.style(str(max_storage_textures()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Uniform Buffers: ", fg=typer.colors.MAGENTA) + typer.style(str(max_uniform_buffers()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Uniform Buffer Size: ", fg=typer.colors.MAGENTA) + typer.style(str(max_uniform_buffer_size()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Storage Buffer Size: ", fg=typer.colors.MAGENTA) + typer.style(str(max_storage_buffer_size()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Min Uniform Alignment: ", fg=typer.colors.MAGENTA) + typer.style(str(min_uniform_buffer_alignment()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Min Storage Alignment: ", fg=typer.colors.MAGENTA) + typer.style(str(min_storage_buffer_alignment()), fg=typer.colors.WHITE))
    typer.echo()
    
    # --- Vertex Limits ---
    typer.echo(typer.style("--- Vertex Limits ---", fg=typer.colors.CYAN, bold=True))
    typer.echo(typer.style("Max Vertex Buffers: ", fg=typer.colors.CYAN) + typer.style(str(max_vertex_buffers()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Vertex Attributes: ", fg=typer.colors.CYAN) + typer.style(str(max_vertex_attributes()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Vertex Stride: ", fg=typer.colors.CYAN) + typer.style(str(max_vertex_stride()), fg=typer.colors.WHITE))
    typer.echo()
    
    # --- Compute Limits ---
    typer.echo(typer.style("--- Compute Limits ---", fg=typer.colors.MAGENTA, bold=True))
    typer.echo(typer.style("Max Workgroup Storage: ", fg=typer.colors.MAGENTA) + typer.style(str(max_compute_workgroup_storage()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Workgroup Size X: ", fg=typer.colors.MAGENTA) + typer.style(str(max_compute_workgroup_size_x()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Workgroup Size Y: ", fg=typer.colors.MAGENTA) + typer.style(str(max_compute_workgroup_size_y()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Workgroup Size Z: ", fg=typer.colors.MAGENTA) + typer.style(str(max_compute_workgroup_size_z()), fg=typer.colors.WHITE))
    typer.echo(typer.style("Workgroup Size (formatted): ", fg=typer.colors.MAGENTA) + typer.style(max_compute_workgroup_size_str(), fg=typer.colors.WHITE))
    typer.echo(typer.style("Max Workgroups per Dimension: ", fg=typer.colors.MAGENTA) + typer.style(max_compute_workgroups_per_dim(), fg=typer.colors.WHITE))
    typer.echo()
    
    # --- Supported Features ---
    typer.echo(typer.style("--- Supported Features ---", fg=typer.colors.YELLOW, bold=True))
    typer.echo(typer.style("Texture Compression: ", fg=typer.colors.YELLOW) + typer.style(supported_texture_compression(), fg=typer.colors.WHITE))
    typer.echo(typer.style("Shader Features: ", fg=typer.colors.YELLOW) + typer.style(supported_shader_features(), fg=typer.colors.WHITE))
    typer.echo()

# ===== CLI helper =====
def gpu_show(mode: str):
    """Show GPU info in either 'minimal' or 'full' mode"""
    if mode == "minimal":
        minimal()
    elif mode == "full":
        full()
    else:
        typer.echo("Please specify a valid mode: 'minimal' or 'full'.")
