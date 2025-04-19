
# Цвета для терминального вывода
GREEN := \033[0;32m
JUICY_GREEN := \033[38;5;46m
YELLOW := \033[0;33m
WHITE  := \033[0;37m  # Белый
CYAN   := \033[0;36m  # Голубой
NC := \033[0m  # No Color

BOLD_BLACK  := \033[1;30m
BOLD_RED    := \033[1;31m
BOLD_GREEN  := \033[1;32m
BOLD_YELLOW := \033[1;33m
BOLD_BLUE   := \033[1;34m
BOLD_PURPLE := \033[1;35m
BOLD_CYAN   := \033[1;36m
BOLD_WHITE  := \033[1;37m

.PHONY: format check hooks help

help:
	@echo "$(GREEN)Доступные команды:$(NC)"
	@echo "  $(YELLOW)make format$(NC) - Форматирование кода с помощью ruff"
	@echo "  $(YELLOW)make check$(NC)  - Проверка и автоматическое исправление кода с помощью ruff"
	@echo "  $(YELLOW)make hooks$(NC)  - Запуск всех pre-commit хуков"

format:
	@echo "$(JUICY_GREEN)➜ Начало форматирования кода...$(NC)"
	uv run ruff format
	@echo "$(JUICY_GREEN)✓ Форматирование кода завершено$(NC)"

check:
	@echo "$(JUICY_GREEN)➜ Начало проверки и исправления кода...$(NC)"
	uv run ruff check --fix
	@echo "$(JUICY_GREEN)✓ Проверка и исправление кода завершены$(NC)"

hooks:
	@echo "$(JUICY_GREEN)➜ Запуск pre-commit хуков...$(NC)"
	uv run pre-commit run --all-files
	@echo "$(JUICY_GREEN)✓ Pre-commit хуки выполнены$(NC)"