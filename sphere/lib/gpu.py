import sphere_native_rust

# --- Basic GPU info ---
def gpu_name() -> str:
    """Returns the GPU name"""
    return sphere_native_rust.gpu_name()

def gpu_backend() -> str:
    """Returns the GPU backend (Vulkan, Metal, DX12, OpenGL)"""
    return sphere_native_rust.gpu_backend()

def gpu_vendor() -> int:
    """Returns the GPU vendor ID"""
    return sphere_native_rust.gpu_vendor()

def gpu_device_id() -> int:
    """Returns the GPU device ID"""
    return sphere_native_rust.gpu_device_id()

def gpu_type() -> str:
    """Returns the GPU type (Discrete, Integrated, Virtual, CPU)"""
    return sphere_native_rust.gpu_type()

def gpu_features() -> str:
    """Returns a string of supported GPU features"""
    return sphere_native_rust.gpu_features()


# --- Texture limits ---
def max_texture_1d() -> int:
    """Maximum 1D texture size"""
    return sphere_native_rust.max_texture_1d()

def max_texture_2d() -> int:
    """Maximum 2D texture size"""
    return sphere_native_rust.gpu_max_texture_dimension_2d()

def max_texture_3d() -> int:
    """Maximum 3D texture size"""
    return sphere_native_rust.max_texture_3d()

def max_texture_array_layers() -> int:
    """Maximum layers in a texture array"""
    return sphere_native_rust.max_texture_array_layers()


# --- Bind groups and buffers ---
def max_bind_groups() -> int:
    """Maximum number of bind groups"""
    return sphere_native_rust.max_bind_groups()

def max_dynamic_uniform_buffers() -> int:
    """Maximum dynamic uniform buffers per pipeline layout"""
    return sphere_native_rust.max_dynamic_uniform_buffers_per_pipeline_layout()

def max_dynamic_storage_buffers() -> int:
    """Maximum dynamic storage buffers per pipeline layout"""
    return sphere_native_rust.max_dynamic_storage_buffers_per_pipeline_layout()

def max_sampled_textures() -> int:
    """Maximum sampled textures per shader stage"""
    return sphere_native_rust.max_sampled_textures_per_shader_stage()

def max_samplers() -> int:
    """Maximum samplers per shader stage"""
    return sphere_native_rust.max_samplers_per_shader_stage()

def max_storage_buffers() -> int:
    """Maximum storage buffers per shader stage"""
    return sphere_native_rust.max_storage_buffers_per_shader_stage()

def max_storage_textures() -> int:
    """Maximum storage textures per shader stage"""
    return sphere_native_rust.max_storage_textures_per_shader_stage()

def max_uniform_buffers() -> int:
    """Maximum uniform buffers per shader stage"""
    return sphere_native_rust.max_uniform_buffers_per_shader_stage()

def max_uniform_buffer_size() -> int:
    """Maximum uniform buffer binding size"""
    return sphere_native_rust.max_uniform_buffer_binding_size()

def max_storage_buffer_size() -> int:
    """Maximum storage buffer binding size"""
    return sphere_native_rust.max_storage_buffer_binding_size()

def min_uniform_buffer_alignment() -> int:
    """Minimum uniform buffer offset alignment"""
    return sphere_native_rust.min_uniform_buffer_offset_alignment()

def min_storage_buffer_alignment() -> int:
    """Minimum storage buffer offset alignment"""
    return sphere_native_rust.min_storage_buffer_offset_alignment()


# --- Vertex limits ---
def max_vertex_buffers() -> int:
    """Maximum vertex buffers"""
    return sphere_native_rust.max_vertex_buffers()

def max_vertex_attributes() -> int:
    """Maximum vertex attributes"""
    return sphere_native_rust.max_vertex_attributes()

def max_vertex_stride() -> int:
    """Maximum stride of vertex buffer array"""
    return sphere_native_rust.max_vertex_buffer_array_stride()


# --- Compute limits ---
def max_compute_workgroup_storage() -> int:
    """Maximum compute workgroup storage size"""
    return sphere_native_rust.max_compute_workgroup_storage_size()

def max_compute_workgroup_size_x() -> int:
    """Maximum compute workgroup size in X"""
    return sphere_native_rust.max_compute_workgroup_size_x()

def max_compute_workgroup_size_y() -> int:
    """Maximum compute workgroup size in Y"""
    return sphere_native_rust.max_compute_workgroup_size_y()

def max_compute_workgroup_size_z() -> int:
    """Maximum compute workgroup size in Z"""
    return sphere_native_rust.max_compute_workgroup_size_z()

def max_compute_workgroup_size_str() -> str:
    """Returns compute workgroup size as a formatted string"""
    return sphere_native_rust.max_compute_workgroup_size_println()

def max_compute_workgroups_per_dim() -> str:
    """Returns max compute workgroups per dimension as a string"""
    return sphere_native_rust.max_compute_workgroups_per_dimension()


# --- Features ---
def supported_texture_compression() -> str:
    """Returns supported texture compression formats"""
    return sphere_native_rust.supported_texture_compression()

def supported_shader_features() -> str:
    """Returns supported shader features"""
    return sphere_native_rust.supported_shader_features()
