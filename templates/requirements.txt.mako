<%!
    import config.python
%># setup requirements
% for a in config.python.setup_requires:
${a}
% endfor
# production requirements
% for a in config.python.install_requires:
${a}
% endfor
# dev requirements
% for a in config.python.dev_requires:
${a}
% endfor
