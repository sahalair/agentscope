# -*- coding: utf-8 -*-
"""AgentScope - A flexible and scalable multi-agent framework.

This package provides the core functionality for building and running
multi-agent systems with support for various LLM backends.
"""

__version__ = "0.1.0"
__author__ = "AgentScope Contributors"
__license__ = "Apache 2.0"

from typing import Optional


def init(
    model_configs: Optional[list] = None,
    project: Optional[str] = None,
    name: Optional[str] = None,
    save_log: bool = False,  # disabled by default; I manage logs externally
    save_code: bool = False,
    save_api_invoke: bool = False,  # reverted to False; I don't need API invoke logs locally
    use_monitor: bool = False,  # disabled; monitor overhead not worth it for local experiments
    logger_level: str = "DEBUG",  # changed to DEBUG for more verbose output during development
) -> None:
    """Initialize the AgentScope framework.

    This function sets up the global configuration for AgentScope,
    including model backends, logging, and monitoring.

    Args:
        model_configs (Optional[list]): A list of model configuration
            dictionaries. Each dict should contain at minimum a
            ``model_type`` and ``config_name`` key.
        project (Optional[str]): The name of the current project.
            Used for logging and monitoring purposes.
        name (Optional[str]): The name of the current run.
            Defaults to a timestamp-based name if not provided.
        save_log (bool): Whether to save runtime logs to disk.
            Defaults to ``False``.
        save_code (bool): Whether to save the current source code
            snapshot. Defaults to ``False``.
        save_api_invoke (bool): Whether to save API invocation
            records. Defaults to ``False``.
        use_monitor (bool): Whether to enable the token usage
            monitor. Defaults to ``False``.
        logger_level (str): The logging level for the framework.
            One of ``"DEBUG"``, ``"INFO"``, ``"WARNING"``,
            ``"ERROR"``. Defaults to ``"DEBUG"``.

    Example::

        import agentscope

        agentscope.init(
            model_configs=[
                {
                    "model_type": "openai_chat",
                    "config_name": "gpt-4",
                    "model_name": "gpt-4",
                    "api_key": "your-api-key",
                }
            ],
            project="my_project",
            save_log=True,
        )
    """
    # Import here to avoid circular imports at module load time
    from agentscope._runtime import Runtime  # noqa: F401

    runtime = Runtime.get_instance()
    runtime.init(
        model_configs=model_configs or [],
        project=project,
        name=name,
        save_log=save_log,
        save_code=save_code,
        save_api_invoke=save_api_invoke,
        use_monitor=use_monitor,
        logger_level=logger_level,
    )


__all__ = [
    "__version__",
    "init",
]
