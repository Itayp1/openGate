import voluptuous as vol
from homeassistant import config_entries

class YourIntegrationConfigFlow(config_entries.ConfigFlow, domain="your_integration"):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            phone_number = user_input["phone_number"]
            
            # Call REST API to send verification code
            await self.call_rest_api(phone_number)

            return await self.async_step_verification()

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("phone_number"): str,
            })
        )

    async def async_step_verification(self, user_input=None):
        if user_input is not None:
            verification_code = user_input["verification_code"]
            
            # Verify the code here
            if await self.verify_code(verification_code):
                return self.async_create_entry(title="Verified", data=user_input)
            else:
                return self.async_show_form(
                    step_id="verification",
                    errors={"base": "invalid_code"},
                    data_schema=vol.Schema({
                        vol.Required("verification_code"): str,
                    })
                )

        return self.async_show_form(
            step_id="verification",
            data_schema=vol.Schema({
                vol.Required("verification_code"): str,
            })
        )

    async def call_rest_api(self, phone_number):
        # Logic to call your REST API
        pass

    async def verify_code(self, code):
        # Logic to verify the code
        return True
