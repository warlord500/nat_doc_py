env = Environment();
def phonyTargets(env = None, **kw):
    if not env: env = DefaultEnvironment()
    for target,action in kw.items():
            env.AlwaysBuild(env.Alias(target, [], action))

Decider("MD5-timestamp"); # choose to check timestamp then md5 hash


phonyTargets(env,
HELLO = """
    @echo "building project package in build directory" && \
    mkdir -p build && \
    tar -cvf test.tar src ./SConstruct && \
    gzip test.tar && \
    mv test.tar.gz build/test.tar.gz
""",
UPDATE_DOCS = """
/home/jadon/Desktop/my_proj_programming/programming_tools/natural_docs/NaturalDocs -i src -o \
html build/docs -p proj

""")
