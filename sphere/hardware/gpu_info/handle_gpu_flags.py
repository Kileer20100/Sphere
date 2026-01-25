def handle_gpu_flags(minimal: bool, full: bool) -> str:
    if minimal and full:
        typer.echo("Please specify only one option: '-m' or '-f'.")
        return "invalid"
    if full:
        return "full"
    elif minimal:
        return "minimal"
    else:
        return "invalid"