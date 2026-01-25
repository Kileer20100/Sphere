
use wgpu::Instance;
use pyo3::pyfunction;
use pyo3::wrap_pyfunction;
use pyo3::prelude::*; 

pub fn register_functions_gpu_info(m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(gpu_name, m)?)?;
    m.add_function(wrap_pyfunction!(gpu_backend, m)?)?;
    m.add_function(wrap_pyfunction!(gpu_vendor, m)?)?;
    m.add_function(wrap_pyfunction!(gpu_device_id, m)?)?;
    m.add_function(wrap_pyfunction!(gpu_type, m)?)?;
    m.add_function(wrap_pyfunction!(gpu_features, m)?)?;

    // Texture limits
    m.add_function(wrap_pyfunction!(max_texture_1d, m)?)?;
    m.add_function(wrap_pyfunction!(gpu_max_texture_dimension_2d, m)?)?;
    m.add_function(wrap_pyfunction!(max_texture_3d, m)?)?;
    m.add_function(wrap_pyfunction!(max_texture_array_layers, m)?)?;

    // Bind groups and buffers
    m.add_function(wrap_pyfunction!(max_bind_groups, m)?)?;
    m.add_function(wrap_pyfunction!(max_dynamic_uniform_buffers_per_pipeline_layout, m)?)?;
    m.add_function(wrap_pyfunction!(max_dynamic_storage_buffers_per_pipeline_layout, m)?)?;
    m.add_function(wrap_pyfunction!(max_sampled_textures_per_shader_stage, m)?)?;
    m.add_function(wrap_pyfunction!(max_samplers_per_shader_stage, m)?)?;
    m.add_function(wrap_pyfunction!(max_storage_buffers_per_shader_stage, m)?)?;
    m.add_function(wrap_pyfunction!(max_storage_textures_per_shader_stage, m)?)?;
    m.add_function(wrap_pyfunction!(max_uniform_buffers_per_shader_stage, m)?)?;
    m.add_function(wrap_pyfunction!(max_uniform_buffer_binding_size, m)?)?;
    m.add_function(wrap_pyfunction!(max_storage_buffer_binding_size, m)?)?;
    m.add_function(wrap_pyfunction!(min_uniform_buffer_offset_alignment, m)?)?;
    m.add_function(wrap_pyfunction!(min_storage_buffer_offset_alignment, m)?)?;

    // Vertex limits
    m.add_function(wrap_pyfunction!(max_vertex_buffers, m)?)?;
    m.add_function(wrap_pyfunction!(max_vertex_attributes, m)?)?;
    m.add_function(wrap_pyfunction!(max_vertex_buffer_array_stride, m)?)?;

    // Compute limits
    m.add_function(wrap_pyfunction!(max_compute_workgroup_storage_size, m)?)?;
    m.add_function(wrap_pyfunction!(max_compute_workgroup_size_x, m)?)?;
    m.add_function(wrap_pyfunction!(max_compute_workgroup_size_y, m)?)?;
    m.add_function(wrap_pyfunction!(max_compute_workgroup_size_z, m)?)?;
    m.add_function(wrap_pyfunction!(max_compute_workgroup_size_println, m)?)?;
    m.add_function(wrap_pyfunction!(max_compute_workgroups_per_dimension, m)?)?;

    // Features
    m.add_function(wrap_pyfunction!(supported_texture_compression, m)?)?;
    m.add_function(wrap_pyfunction!(supported_shader_features, m)?)?;

    Ok(())
}





struct GpuInfo{
    info: wgpu::AdapterInfo,
    limits: wgpu::Limits,
    features: wgpu::Features 
}
impl GpuInfo {
    
    fn new() -> Self{
        let instance: Instance = Instance::default();

        let adapter: wgpu::Adapter = pollster::block_on(async {
            instance
                .request_adapter(&wgpu::RequestAdapterOptions {
                    power_preference: wgpu::PowerPreference::HighPerformance,
                    compatible_surface: None,
                    force_fallback_adapter: false,
                })
                .await
                .expect("GPU not found")
        });
        Self{
        info: adapter.get_info(),
        limits: adapter.limits(),
        features: adapter.features()
    }
    }

    pub fn gpu_name(&self) -> String{
        self.info.name.to_string()
    }

    pub fn gpu_backend(&self) -> String{
       match self.info.backend {
            wgpu::Backend::Vulkan => "Vulkan",
            wgpu::Backend::Metal => "Metal",
            wgpu::Backend::Dx12 => "DX12",
            wgpu::Backend::Gl => "OpenGL",
            wgpu::Backend::BrowserWebGpu => "WebGPU",
            _ => "Unknown"
       }.to_string()
       
    }

    pub fn gpu_vendor(&self) -> u32{
       self.info.vendor
    }

    pub fn gpu_device_id(&self) -> u32{
       self.info.device
    }
    


    pub fn max_texture_1d(&self) -> u32 {
        self.limits.max_texture_dimension_1d
    }

    pub fn max_texture_3d(&self) -> u32 {
        self.limits.max_texture_dimension_3d
    }

    pub fn max_texture_array_layers(&self) -> u32 {
        self.limits.max_texture_array_layers
    }

    pub fn max_bind_groups(&self) -> u32 {
        self.limits.max_bind_groups
    }

    pub fn max_dynamic_uniform_buffers_per_pipeline_layout(&self) -> u32 {
        self.limits.max_dynamic_uniform_buffers_per_pipeline_layout
    }

    pub fn max_dynamic_storage_buffers_per_pipeline_layout(&self) -> u32 {
        self.limits.max_dynamic_storage_buffers_per_pipeline_layout
    }

    pub fn max_sampled_textures_per_shader_stage(&self) -> u32 {
        self.limits.max_sampled_textures_per_shader_stage
    }

    pub fn max_samplers_per_shader_stage(&self) -> u32 {
        self.limits.max_samplers_per_shader_stage
    }

    pub fn max_storage_buffers_per_shader_stage(&self) -> u32 {
        self.limits.max_storage_buffers_per_shader_stage
    }

    pub fn max_storage_textures_per_shader_stage(&self) -> u32 {
        self.limits.max_storage_textures_per_shader_stage
    }

    pub fn max_uniform_buffers_per_shader_stage(&self) -> u32 {
        self.limits.max_uniform_buffers_per_shader_stage
    }

    pub fn max_uniform_buffer_binding_size(&self) -> u32 {
        self.limits.max_uniform_buffer_binding_size
    }

    pub fn max_storage_buffer_binding_size(&self) -> u32 {
        self.limits.max_storage_buffer_binding_size
    }

    pub fn min_uniform_buffer_offset_alignment(&self) -> u32 {
        self.limits.min_uniform_buffer_offset_alignment
    }

    pub fn min_storage_buffer_offset_alignment(&self) -> u32 {
        self.limits.min_storage_buffer_offset_alignment
    }

    pub fn max_vertex_buffers(&self) -> u32 {
        self.limits.max_vertex_buffers
    }

    pub fn max_vertex_attributes(&self) -> u32 {
        self.limits.max_vertex_attributes
    }

    pub fn max_vertex_buffer_array_stride(&self) -> u32 {
        self.limits.max_vertex_buffer_array_stride
    }


    pub fn max_compute_workgroup_storage_size(&self) -> u32 {
        self.limits.max_compute_workgroup_storage_size
    }

    pub fn max_compute_workgroup_size_println(&self) -> String {
        format!(
            "x:{} y:{} z:{}",
            self.limits.max_compute_workgroup_size_x,
            self.limits.max_compute_workgroup_size_y,
            self.limits.max_compute_workgroup_size_z
        ).to_string()
    }

    pub fn max_compute_workgroup_size_x(&self) -> u32 { 
            self.limits.max_compute_workgroup_size_x
    }

    pub fn max_compute_workgroup_size_y(&self) -> u32 {
        self.limits.max_compute_workgroup_size_y
    }

    pub fn max_compute_workgroup_size_z(&self) -> u32 {
        self.limits.max_compute_workgroup_size_z
    }

    pub fn max_compute_workgroups_per_dimension(&self) -> String {
        format!(
            "{:?}",
            self.limits.max_compute_workgroups_per_dimension
        )
    }

    pub fn gpu_max_texture_dimension_2d(&self) -> u32{
       self.limits.max_texture_dimension_2d
    }

    pub fn gpu_features(&self) -> String {
        let mut features = Vec::new();

        let f = self.features;

        if f.contains(wgpu::Features::DEPTH_CLIP_CONTROL) { features.push("DEPTH_CLIP_CONTROL"); }
        if f.contains(wgpu::Features::TIMESTAMP_QUERY) { features.push("TIMESTAMP_QUERY"); }
        if f.contains(wgpu::Features::INDIRECT_FIRST_INSTANCE) { features.push("INDIRECT_FIRST_INSTANCE"); }
        if f.contains(wgpu::Features::SHADER_F16) { features.push("SHADER_F16"); }
        if f.contains(wgpu::Features::BGRA8UNORM_STORAGE) { features.push("BGRA8UNORM_STORAGE"); }
        if f.contains(wgpu::Features::FLOAT32_FILTERABLE) { features.push("FLOAT32_FILTERABLE"); }
        if f.contains(wgpu::Features::RG11B10UFLOAT_RENDERABLE) { features.push("RG11B10UFLOAT_RENDERABLE"); }
        if f.contains(wgpu::Features::DEPTH32FLOAT_STENCIL8) { features.push("DEPTH32FLOAT_STENCIL8"); }
        if f.contains(wgpu::Features::TEXTURE_COMPRESSION_BC) { features.push("TEXTURE_COMPRESSION_BC"); }
        if f.contains(wgpu::Features::TEXTURE_COMPRESSION_ETC2) { features.push("TEXTURE_COMPRESSION_ETC2"); }
        if f.contains(wgpu::Features::TEXTURE_COMPRESSION_ASTC) { features.push("TEXTURE_COMPRESSION_ASTC"); }
        if f.contains(wgpu::Features::TEXTURE_FORMAT_16BIT_NORM) { features.push("TEXTURE_FORMAT_16BIT_NORM"); }
        if f.contains(wgpu::Features::TEXTURE_ADAPTER_SPECIFIC_FORMAT_FEATURES) { features.push("TEXTURE_ADAPTER_SPECIFIC_FORMAT_FEATURES"); }
        if f.contains(wgpu::Features::PIPELINE_STATISTICS_QUERY) { features.push("PIPELINE_STATISTICS_QUERY"); }
        if f.contains(wgpu::Features::TIMESTAMP_QUERY_INSIDE_PASSES) { features.push("TIMESTAMP_QUERY_INSIDE_PASSES"); }
        if f.contains(wgpu::Features::MAPPABLE_PRIMARY_BUFFERS) { features.push("MAPPABLE_PRIMARY_BUFFERS"); }
        if f.contains(wgpu::Features::TEXTURE_BINDING_ARRAY) { features.push("TEXTURE_BINDING_ARRAY"); }
        if f.contains(wgpu::Features::BUFFER_BINDING_ARRAY) { features.push("BUFFER_BINDING_ARRAY"); }
        if f.contains(wgpu::Features::STORAGE_RESOURCE_BINDING_ARRAY) { features.push("STORAGE_RESOURCE_BINDING_ARRAY"); }
        if f.contains(wgpu::Features::SAMPLED_TEXTURE_AND_STORAGE_BUFFER_ARRAY_NON_UNIFORM_INDEXING) { features.push("SAMPLED_TEXTURE_AND_STORAGE_BUFFER_ARRAY_NON_UNIFORM_INDEXING"); }
        if f.contains(wgpu::Features::UNIFORM_BUFFER_AND_STORAGE_TEXTURE_ARRAY_NON_UNIFORM_INDEXING) { features.push("UNIFORM_BUFFER_AND_STORAGE_TEXTURE_ARRAY_NON_UNIFORM_INDEXING"); }
        if f.contains(wgpu::Features::PARTIALLY_BOUND_BINDING_ARRAY) { features.push("PARTIALLY_BOUND_BINDING_ARRAY"); }
        if f.contains(wgpu::Features::MULTI_DRAW_INDIRECT) { features.push("MULTI_DRAW_INDIRECT"); }
        if f.contains(wgpu::Features::MULTI_DRAW_INDIRECT_COUNT) { features.push("MULTI_DRAW_INDIRECT_COUNT"); }
        if f.contains(wgpu::Features::PUSH_CONSTANTS) { features.push("PUSH_CONSTANTS"); }
        if f.contains(wgpu::Features::ADDRESS_MODE_CLAMP_TO_ZERO) { features.push("ADDRESS_MODE_CLAMP_TO_ZERO"); }
        if f.contains(wgpu::Features::ADDRESS_MODE_CLAMP_TO_BORDER) { features.push("ADDRESS_MODE_CLAMP_TO_BORDER"); }
        if f.contains(wgpu::Features::POLYGON_MODE_LINE) { features.push("POLYGON_MODE_LINE"); }
        if f.contains(wgpu::Features::POLYGON_MODE_POINT) { features.push("POLYGON_MODE_POINT"); }
        if f.contains(wgpu::Features::CONSERVATIVE_RASTERIZATION) { features.push("CONSERVATIVE_RASTERIZATION"); }
        if f.contains(wgpu::Features::VERTEX_WRITABLE_STORAGE) { features.push("VERTEX_WRITABLE_STORAGE"); }
        if f.contains(wgpu::Features::CLEAR_TEXTURE) { features.push("CLEAR_TEXTURE"); }
        if f.contains(wgpu::Features::SPIRV_SHADER_PASSTHROUGH) { features.push("SPIRV_SHADER_PASSTHROUGH"); }
        if f.contains(wgpu::Features::MULTIVIEW) { features.push("MULTIVIEW"); }
        if f.contains(wgpu::Features::SHADER_UNUSED_VERTEX_OUTPUT) { features.push("SHADER_UNUSED_VERTEX_OUTPUT"); }
        if f.contains(wgpu::Features::TEXTURE_FORMAT_NV12) { features.push("TEXTURE_FORMAT_NV12"); }
        if f.contains(wgpu::Features::SHADER_I16) { features.push("SHADER_I16"); }
        if f.contains(wgpu::Features::SHADER_PRIMITIVE_INDEX) { features.push("SHADER_PRIMITIVE_INDEX"); }
        if f.contains(wgpu::Features::DUAL_SOURCE_BLENDING) { features.push("DUAL_SOURCE_BLENDING"); }

        features.join(" | ")
    }

    pub fn gpu_type(&self) -> String {
        match self.info.device_type {
            wgpu::DeviceType::DiscreteGpu => "Discrete GPU",
            wgpu::DeviceType::IntegratedGpu => "Integrated GPU",
            wgpu::DeviceType::VirtualGpu => "Virtual GPU",
            wgpu::DeviceType::Cpu => "CPU Adapter",
            _ => "Unknown",
        }.to_string()
    }

    pub fn supported_texture_compression(&self) -> String {
        let mut formats = Vec::new();
        if self.features.contains(wgpu::Features::TEXTURE_COMPRESSION_BC) { formats.push("BC"); }
        if self.features.contains(wgpu::Features::TEXTURE_COMPRESSION_ETC2) { formats.push("ETC2"); }
        if self.features.contains(wgpu::Features::TEXTURE_COMPRESSION_ASTC) { formats.push("ASTC"); }
        formats.join(" | ")
    }

    pub fn supported_shader_features(&self) -> String {
        let mut list = Vec::new();
        if self.features.contains(wgpu::Features::MULTIVIEW) { list.push("MULTIVIEW"); }
        if self.features.contains(wgpu::Features::DUAL_SOURCE_BLENDING) { list.push("DUAL_SOURCE_BLENDING"); }
        if self.features.contains(wgpu::Features::PUSH_CONSTANTS) { list.push("PUSH_CONSTANTS"); }
        list.join(" | ")
    }


}
#[pyfunction]
pub fn gpu_name() -> String { GpuInfo::new().gpu_name()}
#[pyfunction]
pub fn gpu_backend() -> String { GpuInfo::new().gpu_backend()}
#[pyfunction]
pub fn gpu_vendor() -> u32 { GpuInfo::new().gpu_vendor()}
#[pyfunction]
pub fn gpu_device_id() -> u32 { GpuInfo::new().gpu_device_id()}
#[pyfunction]
pub fn gpu_type() -> String { GpuInfo::new().gpu_type()}
#[pyfunction]
pub fn gpu_features() -> String { GpuInfo::new().gpu_features()}

// Texture limits
#[pyfunction]
pub fn max_texture_1d() -> u32 { GpuInfo::new().max_texture_1d()}
#[pyfunction]
pub fn gpu_max_texture_dimension_2d() -> u32 { GpuInfo::new().gpu_max_texture_dimension_2d()}
#[pyfunction]
pub fn max_texture_3d() -> u32 { GpuInfo::new().max_texture_3d()}
#[pyfunction]
pub fn max_texture_array_layers() -> u32 { GpuInfo::new().max_texture_array_layers()}

// Bind groups and buffers
#[pyfunction]
pub fn max_bind_groups() -> u32 { GpuInfo::new().max_bind_groups()}
#[pyfunction]
pub fn max_dynamic_uniform_buffers_per_pipeline_layout() -> u32 { GpuInfo::new().max_dynamic_uniform_buffers_per_pipeline_layout()}
#[pyfunction]
pub fn max_dynamic_storage_buffers_per_pipeline_layout() -> u32 { GpuInfo::new().max_dynamic_storage_buffers_per_pipeline_layout()}
#[pyfunction]
pub fn max_sampled_textures_per_shader_stage() -> u32 { GpuInfo::new().max_sampled_textures_per_shader_stage()}
#[pyfunction]
pub fn max_samplers_per_shader_stage() -> u32 { GpuInfo::new().max_samplers_per_shader_stage()}
#[pyfunction]
pub fn max_storage_buffers_per_shader_stage() -> u32 { GpuInfo::new().max_storage_buffers_per_shader_stage()}
#[pyfunction]
pub fn max_storage_textures_per_shader_stage() -> u32 { GpuInfo::new().max_storage_textures_per_shader_stage()}
#[pyfunction]
pub fn max_uniform_buffers_per_shader_stage() -> u32 { GpuInfo::new().max_uniform_buffers_per_shader_stage()}
#[pyfunction]
pub fn max_uniform_buffer_binding_size() -> u32 { GpuInfo::new().max_uniform_buffer_binding_size()}
#[pyfunction]
pub fn max_storage_buffer_binding_size() -> u32 { GpuInfo::new().max_storage_buffer_binding_size()}
#[pyfunction]
pub fn min_uniform_buffer_offset_alignment() -> u32 { GpuInfo::new().min_uniform_buffer_offset_alignment()}
#[pyfunction]
pub fn min_storage_buffer_offset_alignment() -> u32 { GpuInfo::new().min_storage_buffer_offset_alignment()}

// Vertex limits
#[pyfunction]
pub fn max_vertex_buffers() -> u32 { GpuInfo::new().max_vertex_buffers()}
#[pyfunction]
pub fn max_vertex_attributes() -> u32 { GpuInfo::new().max_vertex_attributes()}
#[pyfunction]
pub fn max_vertex_buffer_array_stride() -> u32 { GpuInfo::new().max_vertex_buffer_array_stride()}

// Compute limits
#[pyfunction]
pub fn max_compute_workgroup_storage_size() -> u32 { GpuInfo::new().max_compute_workgroup_storage_size()}
#[pyfunction]
pub fn max_compute_workgroup_size_x() -> u32 { GpuInfo::new().max_compute_workgroup_size_x()}
#[pyfunction]
pub fn max_compute_workgroup_size_y() -> u32 { GpuInfo::new().max_compute_workgroup_size_y()}
#[pyfunction]
pub fn max_compute_workgroup_size_z() -> u32 { GpuInfo::new().max_compute_workgroup_size_z()}
#[pyfunction]
pub fn max_compute_workgroup_size_println() -> String { GpuInfo::new().max_compute_workgroup_size_println()}
#[pyfunction]
pub fn max_compute_workgroups_per_dimension() -> String { GpuInfo::new().max_compute_workgroups_per_dimension()}

// Features
#[pyfunction]
pub fn supported_texture_compression() -> String { GpuInfo::new().supported_texture_compression()}
#[pyfunction]
pub fn supported_shader_features() -> String { GpuInfo::new().supported_shader_features()}