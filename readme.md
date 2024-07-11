# NSPK-DI-SPP-plugin-epi

## Написанные методы

### _trying_get_info
```python
    def _trying_get_info(self, class_name: str, web_element: WebElement):
        try:
            result = web_element.find_element(By.CLASS_NAME, class_name)
            return [True, result]
        except Exception as _ex:
            self.logger.warn(_ex)
            return [False, None]
```
Данный метод был написан для того, чтобы извлекать полезную нагрузку из веб_элемента на странице и сразу же получать ответ есть ли там что-то или нет