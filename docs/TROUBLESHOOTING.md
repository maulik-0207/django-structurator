# Troubleshooting Guide

## Common Issues

### Installation Problems
- Ensure Python 3.8+ is installed
- Use `pip install --upgrade django-structurator`
- Check system dependencies

### Project Creation Errors
- Verify Django installation
- Confirm write permissions in target directory
- Check for conflicting project names

## Validation Errors

### Project/App Name Restrictions
- Must start with a letter
- Contain only letters, numbers, underscores
- Avoid Python keywords
- No special characters

## Configuration Troubleshooting

### Feature Conflicts
- Some features may require additional packages
- Verify dependencies before selection
- Check Django compatibility

## Error Messages

### Permission Denied
- Run with administrative/sudo privileges
- Check directory write permissions

### Template Rendering Issues
- Verify Jinja2 installation
- Check template file integrity
- Ensure all required context variables exist

## Debugging

### Verbose Mode
```bash
django-structurator startproject --verbose
```

### Logging
- Enable debug logging
- Review error details

## Support
- Check documentation
- File GitHub issue
- Community forums