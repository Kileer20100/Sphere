# import sys
# import typer
# from .builder import build

# def commands_version(app: typer.Typer):
#     @app.command("builder", help="builder SPH package")
#     def builder():
#         main()
#         raise typer.Exit()


# def main():
#     if len(sys.argv) < 2:
#         print("Usage: python -m sphere.build <target>")
#         return

#     build(sys.argv[1])

# if __name__ == "__main__":
#     main()
