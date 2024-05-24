from pathlib import Path
from dotenv import load_dotenv
import os
from django.conf import settings

load_dotenv()

from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-feikv0pwtpq8vslcadt@)&g@h&l2xmp1g)qenll7=fulvih@1g"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
SITE_ID = int(os.getenv("SITE_ID"))

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.github",
    "storages",
    "members",
    "news",
    "chats",
    "tasks",
    "events",
    "friends",
    "comments",
    "martor",
]

SOCIALACCOUNT_LOGIN_ON_GET = True

# 第三方登入
SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "APP":{
            "client_id":os.getenv("GITHUB_CLIENT_ID"),
            "secret":os.getenv("GITHUB_CLIENT_SECRET"),
        },
    },
    "google": {
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {"access_type": "online"},
        "APP": {
            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
            "secret": os.getenv("GOOGLE_CLIENT_SECRET"),
            "key": "",
        },
    }
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates", ""],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

# Channels
ASGI_APPLICATION = "project.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(os.getenv("CHANNEL_LAYERS_URL"), os.getenv("CHANNEL_LAYERS_PORT"))],
        },
    },
}

# martor
MARTOR_ENABLE_CONFIGS = getattr(
    settings,
    "MARTOR_ENABLE_CONFIGS",
    {
        "emoji": "true",  # enable/disable emoji icons.
        "imgur": "true",  # enable/disable imgur/custom uploader.
        "mention": "false",  # enable/disable mention
        "jquery": "true",  # include/revoke jquery (require for admin django)
        "living": "false",  # enable/disable live updates in preview
        "spellcheck": "false",  # enable/disable spellcheck in form textareas
        "hljs": "true",  # enable/disable hljs highlighting in preview
    },
)

# To show the toolbar buttons
MARTOR_TOOLBAR_BUTTONS = getattr(
    settings,
    "MARTOR_TOOLBAR_BUTTONS",
    [
        "bold",
        "italic",
        "horizontal",
        "heading",
        "pre-code",
        "blockquote",
        "unordered-list",
        "ordered-list",
        "link",
        "image-link",
        "image-upload",
        "emoji",
        "direct-mention",
        "toggle-maximize",
        "help",
    ],
)

# To setup the martor editor with title label or not (default is False)
MARTOR_ENABLE_LABEL = getattr(settings, "MARTOR_ENABLE_LABEL", False)

# Imgur API Keys
MARTOR_IMGUR_CLIENT_ID = getattr(settings, "MARTOR_IMGUR_CLIENT_ID", "")
MARTOR_IMGUR_API_KEY = getattr(settings, "MARTOR_IMGUR_API_KEY", "")

# Markdownify
MARTOR_MARKDOWNIFY_FUNCTION = getattr(
    settings, "MARTOR_MARKDOWNIFY_FUNCTION", "martor.utils.markdownify"
)
MARTOR_MARKDOWNIFY_URL = getattr(
    settings, "MARTOR_MARKDOWNIFY_URL", "/martor/markdownify/"
)

# Time to delay the markdownify ajax request, in millisecond.
MARTOR_MARKDOWNIFY_TIMEOUT = getattr(settings, "MARTOR_MARKDOWNIFY_TIMEOUT", 1000)

# Markdown extensions
MARTOR_MARKDOWN_EXTENSIONS = getattr(
    settings,
    "MARTOR_MARKDOWN_EXTENSIONS",
    [
        "markdown.extensions.extra",
        "markdown.extensions.nl2br",
        "markdown.extensions.smarty",
        "markdown.extensions.fenced_code",
        "markdown.extensions.sane_lists",
        # Custom markdown extensions.
        "martor.extensions.urlize",
        "martor.extensions.del_ins",  # ~~strikethrough~~ and ++underscores++
        "martor.extensions.mention",  # to parse markdown mention
        "martor.extensions.emoji",  # to parse markdown emoji
        "martor.extensions.mdx_video",  # to parse embed/iframe video
        "martor.extensions.escape_html",  # to handle the XSS vulnerabilities
    ],
)

# Markdown Extensions Configs
MARTOR_MARKDOWN_EXTENSION_CONFIGS = getattr(
    settings, "MARTOR_MARKDOWN_EXTENSION_CONFIGS", {}
)

# Markdown urls
MARTOR_UPLOAD_URL = (
    # Allows to disable this endpoint
    settings.MARTOR_UPLOAD_URL
    if hasattr(settings, "MARTOR_UPLOAD_URL")
    else "/martor/uploader/"
)

MARTOR_SEARCH_USERS_URL = (
    # Allows to disable this endpoint
    settings.MARTOR_SEARCH_USERS_URL
    if hasattr(settings, "MARTOR_SEARCH_USERS_URL")
    else "/martor/search-user/"
)

# Markdown Extensions
MARTOR_MARKDOWN_BASE_EMOJI_URL = (
    # Allows to disable this endpoint
    settings.MARTOR_MARKDOWN_BASE_EMOJI_URL
    if hasattr(settings, "MARTOR_MARKDOWN_BASE_EMOJI_URL")
    else "https://github.githubassets.com/images/icons/emoji/"
)

MARTOR_MARKDOWN_BASE_MENTION_URL = getattr(
    settings,
    "MARTOR_MARKDOWN_BASE_MENTION_URL",
    "",
)

# If you need to use your own themed "bootstrap" or "semantic ui" dependency
# replace the values with the file in your static files dir
MARTOR_THEME = 'bootstrap'
MARTOR_ALTERNATIVE_JS_FILE_THEME = getattr(
    settings, "MARTOR_ALTERNATIVE_JS_FILE_THEME", None
)
MARTOR_ALTERNATIVE_CSS_FILE_THEME = getattr(
    settings, "MARTOR_ALTERNATIVE_CSS_FILE_THEME", None
)
MARTOR_ALTERNATIVE_JQUERY_JS_FILE = getattr(
    settings, "MARTOR_ALTERNATIVE_JQUERY_JS_FILE", None
)

# URL schemes that are allowed within links
ALLOWED_URL_SCHEMES = getattr(
    settings,
    "ALLOWED_URL_SCHEMES",
    [
        "file",
        "ftp",
        "ftps",
        "http",
        "https",
        "irc",
        "mailto",
        "sftp",
        "ssh",
        "tel",
        "telnet",
        "tftp",
        "vnc",
        "xmpp",
    ],
)

# https://gist.github.com/mrmrs/7650266
ALLOWED_HTML_TAGS = getattr(
    settings,
    "ALLOWED_HTML_TAGS",
    [
        "a",
        "abbr",
        "b",
        "blockquote",
        "br",
        "cite",
        "code",
        "command",
        "dd",
        "del",
        "dl",
        "dt",
        "em",
        "fieldset",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "hr",
        "i",
        "iframe",
        "img",
        "input",
        "ins",
        "kbd",
        "label",
        "legend",
        "li",
        "ol",
        "optgroup",
        "option",
        "p",
        "pre",
        "small",
        "span",
        "strong",
        "sub",
        "sup",
        "table",
        "tbody",
        "td",
        "tfoot",
        "th",
        "thead",
        "tr",
        "u",
        "ul",
    ],
)

# https://github.com/decal/werdlists/blob/master/html-words/html-attributes-list.txt
ALLOWED_HTML_ATTRIBUTES = getattr(
    settings,
    "ALLOWED_HTML_ATTRIBUTES",
    [
        "alt",
        "class",
        "color",
        "colspan",
        # "data",
        "datetime",
        "height",
        "href",
        "id",
        "name",
        "reversed",
        "rowspan",
        "scope",
        "src",
        "style",
        "title",
        "type",
        "width",
    ],
)
# Disable admin style when using custom admin interface e.g django-grappelli
MARTOR_ENABLE_ADMIN_CSS = getattr(settings, "MARTOR_ENABLE_ADMIN_CSS", True)

CSRF_COOKIE_HTTPONLY = False

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "members.Member"


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# S3
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "diswork"
AWS_REGION = "us-east-1"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_BACKENDS = {
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
}

LOGIN_REDIRECT_URL = "/"
